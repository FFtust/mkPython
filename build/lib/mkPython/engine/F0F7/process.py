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
    
    def start_engine(self, start_heart = True):
        neuron_request_bind_phy(self.protocol.send_protocol)
        if start_heart:
            neurons_heartbeat_start()

    def process(self, frame, d_info):
        response_distributor(frame)
