#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time
import threading
import signal
import sys

# from utils.mylog import console
from link.base import base_link

IP_DEFAULT = "192.168.4.1"
PORT_DEFAULT = 5050
READ_TIMEOUT_DEFAULT = 0.3

class socket_link(base_link):
    def __init__(self, para):
        self.protocol_list = []
        self.config(para)
        super().__init__()

        self.write_lock = threading.Lock()

        signal.signal(signal.SIGINT, self.signal_handler)
        self.exiting = False


    def signal_handler(self, sig, frame):
        print('You pressed Ctrl+C!')
        self.exiting = True

    '''
    para:[port, baudrate, timeout]
    '''
    def config(self, para = []):
        if not(isinstance(para, (list,tuple)) and len(para) > 0):
            return

        if len(para) == 1:
            para.append(IP_DEFAULT)
            para.append(PORT_DEFAULT)
        elif len(para) == 2:
            para.append(PORT_DEFAULT)

        self.socket = None
        self.ip = para[1]
        self.port = para[2]


        super().config(para)

    def open(self):
        self.socket = socket.socket()
        print((self.ip, self.port))
        if self.socket.connect((self.ip, self.port)):
            print("connect successed: %s, %s" %(self.ip, self.port))
        else:
            print("connect failed: %s, %s" %(self.ip, self.port))

        super().open()

    def close(self, immediate = True):
        self.socket.disconnect()
        super().close()

    def write(self, frame):
        self.write_lock.acquire()
        self.scoket.write(frame)
        self.write_lock.release()

    def read(self, bytes_num = 1):
        data = self.scoket.read(bytes_num)
        return data
    
    def rigister_protocol_parse_handle(self, protocol):
        self.protocol_list.append(protocol)
        protocol.link = self

    def start_listening(self):
        self.thread_work = threading.Thread(target = self.__listening_task, args = (), daemon=True)
        self.thread_work.start()
        
    def stop_listening(self):
        pass

    def __listening_task(self):
        while True:
            if super().get_status() == super()._LINK_STA_CLOSE:
                break

            if self.exiting:
                break
            data_stream = self.read()
            if data_stream == b'':
                continue
            for item in self.protocol_list:
                item.parse_data_stream(data_stream, "uart")
