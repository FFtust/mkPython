from struct import pack, unpack
import time
import re
import os

# cofig if use existed dictionaries
USE_DICT_CREATED_PRIVIOUSLY = True

if USE_DICT_CREATED_PRIVIOUSLY:
    from engine.F0F7.neurons_dicts import general_command_request_dict
    from engine.F0F7.neurons_dicts import general_command_response_dict
    from engine.F0F7.neurons_dicts import common_neurons_command_request_dict
    from engine.F0F7.neurons_dicts import common_neurons_command_response_dict
    from engine.F0F7.neurons_dicts import common_neurons_command_default_result_dict
else:
    general_command_request_dict = dict() 
    general_command_response_dict = dict()

    common_neurons_command_request_dict = dict()
    common_neurons_command_response_dict = dict()
    common_neurons_command_default_result_dict = dict()


online_neurons_module_inactive_block_dict = dict()
online_neurons_module_temporary_result_dict = dict()


def read_general_command_request_to_dict():
    global general_command_request_dict
    uos.chdir("/lib")
    with open("request_general_command.csv", "r") as f:
        line = f.readline()   #read the title line
        line = f.readline()
        while line:
            general_command_request_block_dict = dict()
            line_elements = line.split(',')
            elements_length = len(line_elements)
            general_command_request_block_dict["type"] = int(line_elements[1],16);
            if(line_elements[2] != "None"):
                general_command_request_block_dict["subtype"] = int(line_elements[2],16);
            else:
                general_command_request_block_dict["subtype"] = None;
            para_num = 1
            while line_elements[para_num+2] != "" and \
                  line_elements[para_num+2] != "\r\n" and \
                  (para_num + 2) < elements_length:
                general_command_request_block_dict[para_num] = line_elements[para_num+2];
                para_num = para_num + 1
            general_command_request_block_dict["para_num"] = para_num - 1
            general_command_request_dict[line_elements[0]] = general_command_request_block_dict
           
            line = f.readline()
    f.close( )
    #print(general_command_request_dict)

def read_general_command_response_to_dict():
    global general_command_response_dict
    uos.chdir("/lib")
    with open("response_general_command.csv", "r") as f:
        line = f.readline()   #read the title line
        line = f.readline()
        while line:
            general_command_response_block_dict = dict()
            line_elements = line.split(',')
            elements_length = len(line_elements)
            type_str = (int(line_elements[2],16)) & 0x7f
            if(line_elements[3] != "None"):
                type_str = type_str * 256 + int(line_elements[3],16)
            else:
                type_str = type_str * 256
            general_command_response_block_dict["name"] = line_elements[0]

            para_num = 1
            while line_elements[para_num+3] != "" and \
                  line_elements[para_num+3] != "\r\n" and \
                  (para_num + 3) < elements_length:
                general_command_response_block_dict[para_num] = line_elements[para_num+3];
                para_num = para_num + 1
            general_command_response_block_dict["para_num"] = para_num - 1
            general_command_response_dict[type_str] = general_command_response_block_dict
            line = f.readline()

    #print(general_command_response_dict)
    f.close( )

def read_common_neurons_command_request_to_dict():
    global common_neurons_command_request_dict
    uos.chdir("/lib")
    with open("request_common_neurons_command.csv", "r") as f:
        line = f.readline()   #read the title line
        line = f.readline()
        common_neurons_command_request_block_dict = dict()
        while line:
            common_neurons_command_request_function_dict = dict()
            line_elements = line.split(',')
            elements_length = len(line_elements)

            type_str = (int(line_elements[1],16)) & 0x7f

            if(line_elements[2] != "None"):
                type_str = type_str * 256 + int(line_elements[2],16);
            else:
                type_str = type_str * 256 + 0;

            if type_str in common_neurons_command_request_dict:
                pass
            else:
                common_neurons_command_request_function_dict_list = dict()
                common_neurons_command_request_block_dict = dict()
                common_neurons_command_request_block_dict["name"] =  line_elements[0]

            common_neurons_command_request_function_dict["command_id"] = int(line_elements[4],16);
            
            para_num = 1
            while line_elements[para_num+4] != "" and \
                  line_elements[para_num+4] != "\r\n" and \
                  (para_num + 4) < elements_length:
                common_neurons_command_request_function_dict[para_num] = line_elements[para_num+4];
                para_num = para_num + 1
            common_neurons_command_request_function_dict["para_num"] = para_num - 1
            common_neurons_command_request_function_dict_list[line_elements[3]] = common_neurons_command_request_function_dict
            common_neurons_command_request_block_dict["function"] = common_neurons_command_request_function_dict_list
            common_neurons_command_request_dict[type_str] = common_neurons_command_request_block_dict
           
            line = f.readline()
    f.close( )
    #print(common_neurons_command_request_dict)

def read_common_neurons_command_response_to_dict():
    global common_neurons_command_response_dict
    global common_neurons_command_default_result_dict
    uos.chdir("/lib")
    with open("response_common_neurons_command.csv", "r") as f:
        line = f.readline()   #read the title line
        line = f.readline()
        while line:
            common_neurons_command_response_function_dict = dict()
            line_elements = line.split(',')
            elements_length = len(line_elements)
            type_str = (int(line_elements[2],16)) & 0x7f
            if(line_elements[3] != "None"):
                type_str = type_str * 256 + int(line_elements[3],16);
            else:
                type_str = type_str * 256 + 0;

            if type_str in common_neurons_command_response_dict:
                common_neurons_command_default_function_result_list = []
                pass
            else:
                common_neurons_command_response_function_dict_list = dict()
                common_neurons_command_response_block_dict = dict()
                common_neurons_command_response_block_dict["name"] =  line_elements[0]

                common_neurons_command_default_function_result_list = []
                common_neurons_command_default_block_result_dict = dict()

            common_neurons_command_response_function_dict["command_name"] = line_elements[4];
            para_num = 1
            while line_elements[para_num+5] != "" and \
                  line_elements[para_num+5] != "\r\n" and \
                  (para_num + 5) < elements_length:
                str_para = line_elements[para_num+5];
                pos = str_para.rfind('/')
                if pos == -1:
                    para_type = str_para
                    para_default_value = 0
                else:
                    para_type = str_para[0:pos]
                    para_default_value_str = str_para.split('/')[-1]
                    para_default_value = conversion_str_to_data(para_type, para_default_value_str)
                common_neurons_command_response_function_dict[para_num] = line_elements[para_num+5];
                common_neurons_command_default_function_result_list.append(para_default_value)
                para_num = para_num + 1
            common_neurons_command_response_function_dict["para_num"] = para_num - 1
            common_neurons_command_response_function_dict_list[int(line_elements[5],16)] = common_neurons_command_response_function_dict
            common_neurons_command_response_block_dict["function"] = common_neurons_command_response_function_dict_list
            common_neurons_command_default_block_result_dict[line_elements[4]] = common_neurons_command_default_function_result_list
            common_neurons_command_response_dict[type_str] = common_neurons_command_response_block_dict
            common_neurons_command_default_result_dict[line_elements[0]] = common_neurons_command_default_block_result_dict
            line = f.readline()
    f.close( )
    # print(common_neurons_command_response_dict)