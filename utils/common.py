import time 
import os

# append new lib path
def add_path(path):
    cur_path = os.getcwd()
    if path[:4] == "last":
        level = path.split("-")[1]
        append_path = '\\'.join(o_path.split('\\')[:-level])
    else:
        append_path = path

    print("cur path:", cur_path)
    print("new path:", append_path)

    sys.path.append(append_path)


def wait_max_time(max_time_ms, conditions, tick = None):
    if type(conditions) != "list" and \
       type(conditions) != "tuple":
        conditions = [conditions]

    start = time.time()
    while time.time() - start < (max_time_ms / 1000):
        for item in conditions:
            if callable(item):
                if item():
                    break
            else:
                if item:
                    break

        if tick:
            time.sleep(tick)

# check the range of number
def num_range_check(num, min_n = None, max_n = None, to_range = True):
    if min_n == None and max_n == None:
        return num
    
    if min_n != None:
        if to_range and num < min_n:
            num = min_n

    if max_n != None:
        if to_range and num > max_n:
            num = max_n
    return num

# bytes switch
def float_to_byte_4(data): 
    float_bytes = pack('f', data)
    return bytearray(float_bytes)

def int_to_byte_4(data):
    if type(data) == float:
        data = int(data)
    int_bytes = data.to_bytes(4, "little")
    return bytearray(int_bytes)

def int_to_byte_2(data):
    if type(data) == float:
        data = int(data)
    int_bytes = data.to_bytes(2, "little")
    return bytearray(int_bytes)

def byte_2_to_short(data):
    if len(data) != 2:
        return None
    result = unpack('h', bytearray(data))
    result = result[0]
    return bytearray(result)

def byte_4_to_float(data): 
    float_bytes = unpack('f', bytearray(data))
    result = result[0]
    return bytearray(result)

def byte_4_to_int(data):
    if len(data) != 4:
        return None
    result = unpack('l', bytearray(data))
    result = result[0]
    return bytearray(result)

