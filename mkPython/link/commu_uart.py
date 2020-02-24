#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import time
import threading

from utils.mylog import console
from link.base import base_link

BAUDRATE_DEFAULT = 115200
SERIAL_TIMEOUT_DEFAULT = 0.3

class uart_link(base_link):
    def __init__(self, para):
        self.protocol_list = []
        self.config(para)
        super().__init__()
    
    '''
    para:[port, baudrate, timeout]
    '''
    def config(self, para = []):
        if not(isinstance(para, (list,tuple)) and len(para) > 0):
            return

        if len(para) == 1:
            para.append(BAUDRATE_DEFAULT)
            para.append(SERIAL_TIMEOUT_DEFAULT)
        elif len(para) == 2:
            para.append(SERIAL_TIMEOUT_DEFAULT)

        self.ser = None
        self.com_port = para[0]
        self.baudrate = para[1]

        self.ser = serial.Serial(None, self.baudrate, timeout = SERIAL_TIMEOUT_DEFAULT)
        super().config(para)

    def open(self):
        self.ser.port = self.com_port
        self.ser.baudrate = self.baudrate
        self.ser.write_timeout = SERIAL_TIMEOUT_DEFAULT
        if not self.ser.is_open:
            self.ser.open()

        super().open()

    def close(self):
        if self.ser:
            if self.ser.is_open:
                self.ser.close()

        super().close()

    def write(self, frame):
        if not self.ser.is_open:
            return

        console.warning("phy write frame is: %s" %frame)
        self.ser.write(frame)

    def read(self, bytes_num = 1):
        data = bytearray()
        if self.ser.is_open:
            data = self.ser.read(bytes_num)
        return data
    
    def rigister_protocol_parse_handle(self, protocol):
        self.protocol_list.append(protocol)
        protocol.link = self

    def start_listening(self):
        self.thread_work = threading.Thread(target = self.__listening_task, args = ())
        self.thread_work.start()
        
    def stop_listening(self):
        pass

    def __listening_task(self):
        while True:
            data_stream = self.read()
            if data_stream == b'':
                continue
            for item in self.protocol_list:
                item.parse_data_stream(data_stream, "uart")
