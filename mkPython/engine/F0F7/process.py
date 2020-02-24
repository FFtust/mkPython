#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' neurons transport layout '

import _thread
import time

from engine.F0F7.neurons_engine import response_distributor
from engine.F0F7.neurons_engine import neurons_heartbeat_start
from engine.F0F7.neurons_engine import neuron_request_bind_phy


NEURONS_PROTOCOL_HEAD = 0xf0
NEURONS_PROTOCOL_END = 0xf7


class neurons_process_c:
    def __init__(self):
        self.protocol = None
    
    def start_engine(self):
        neuron_request_bind_phy(self.protocol.send_protocol)
        neurons_heartbeat_start()

    def __get_channel(self, frame):
        return frame[0]
    
    def __get_data_region(self, frame):
        # the first 4 bytes are reserved
        return frame[4:]

    def process(self, frame, d_info):
        # channel = self.__get_channel(frame)
        # data_region = self.__get_data_region(frame)
        # if (not channel) or (not data_region):
        #     pass
        # else:
        response_distributor(frame)
