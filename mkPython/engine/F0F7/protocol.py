# -*- coding: utf-8 -*-
from struct import pack, unpack

from utils.common import int_to_byte_2
from utils.mylog import console


'''
F0F7 frame structure
----*----*----*----*----*----*----*----*----*----*
head|ID  |type|sub |cmd |da_1| ...|da_n|sum |end |   
----*----*----*----*----*----*----*----*----*----*
 F0 | ** | ** | ** | ** | ** | ** | ** | ** | F7 |
----*----*----*----*----*----*----*----*----*----*
description:
'''

F0F7_PROTOCOL_HEAD = 0xF0
F0F7_PROTOCOL_END = 0xF7

class F0F7_frame():
    # about frame limits
    FRAME_MAX_LEN = 1024
    FRAME_MAX_NUM = 32

    # protocol catch FSM state
    FSM_S_HEAD = 0
    FSM_S_DATA = 1
    FSM_S_SUM= 2
    FSM_S_END = 3

    def __init__(self):
        self.link = None
        self.frame_process_list = []
        self.__fsm_init()


    def create_frame(self, data):
        protocol_frame = bytearray(3 + len(data))
        protocol_frame[0] = F0F7_PROTOCOL_HEAD

        check_sum = 0
        for i in range(len(data)):
            protocol_frame[i + 1] = data[i]
            check_sum += data[i]

        check_sum = check_sum & 0x7f
        protocol_frame[-2] = check_sum
        protocol_frame[-1] = 0xF7
        
        return protocol_frame

    def print_frame(self, frame):
        pass
        
    def register_frame_process(self, process, conditions = None):
        process.protocol = self
        self.frame_process_list.append(process)

    def parse_data_stream(self, data, d_info = None):
        self.__fsm(data)
        if self.frame_list:
            console.debug("%s"%self.frame_list)
            for item in self.frame_list:
                for process in self.frame_process_list:
                    ret = process.process(item, d_info)

                    # process result
                    if ret:
                        pass
                self.frame_list.remove(item)

    # FSM processing
    def __fsm_init(self):    
        '''
        frame FSM manager
        '''
        self.fsm_state = self.FSM_S_HEAD
        self.recv_buffer = bytearray()
        self.recv_len = 0
        self.head_checksum = 0
        self.data_region_len = 0

        self.frame_list = []

    # Input a stream data, split stream to frame and save in frame_list
    def __fsm(self, stream):
        # this variable indicate the number of datas should be read next time
        ret_num = 1
        for c in stream:
            receive_frame = None

            if len(self.recv_buffer) > self.FRAME_MAX_LEN:
                self.fsm_state = self.S_HEAD

            if (F0F7_PROTOCOL_HEAD == c):
                self.fsm_state = self.FSM_S_DATA
                self.recv_buffer = bytearray()
                self.fsm_state = self.FSM_S_DATA
            elif (self.fsm_state == self.FSM_S_DATA) and (F0F7_PROTOCOL_END == c):
                check_sum = 0 
                for i in range(len(self.recv_buffer) - 1):
                    check_sum = check_sum + self.recv_buffer[i]
                check_sum = check_sum & 0x7F

                if check_sum == self.recv_buffer[-1]:
                    receive_frame = self.recv_buffer[:-1]
                self.fsm_state = self.FSM_S_HEAD

            elif (self.FSM_S_DATA == self.fsm_state):
                self.recv_buffer.append(c)


            if receive_frame:
                console.debug("F0F7 received frame %s" %receive_frame)
                # frame_list do not contain the protocol structure datas
                self.frame_list.append(receive_frame)

        if len(self.frame_list) > self.FRAME_MAX_NUM:
            console.warning("F0F7 frame list overflow, clear")
            self.frame_list.clear()
        
        return ret_num
    
    def send_protocol(self, package):
        console.debug("send_protocol %s"%package)
        if self.link:
            print(self.create_frame(package))
            self.link.write(self.create_frame(package))



