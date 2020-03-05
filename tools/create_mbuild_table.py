#!/usr/bin/python3.7 
# -*- coding: utf-8 -*- 

import re
import os
import sys
import hashlib

API_DIR = "../mkPython/device/api/mbuild"

def get_api_files():
    api_files = []
    os.chdir(API_DIR)
    for item in os.listdir():
        if os.path.isfile(item):
            api_files.append(item)
    return api_files

def create_from_file(file_name):
    new_file_content = ""

    last_line = ""
    with open(file_name, 'r', encoding='UTF-8') as f:
        for line in f: 
            # get class
            ret = re.match(r'class(.*):', line)
            if ret:
                class_name = re.search(r'(\S*)_c', line).group(0)[0:-2]
                print("class_name", class_name)
            
            else:
                ret = re.search(r'(.*)def(.*):', line)
                if ret:
                    # func = line.split('(')[0]
                    func = re.search(r'\s(\w*)\(', line).group(0)[1:-1]
                    m = hashlib.md5()
                    m.update(("mbuild."+class_name+'.'+func).encode("utf-8"))
                    tag = m.hexdigest()
                    new_file_content += ('"%s": {"key":None, "obj":cell_item("%s", "mbuild.%s.%s", (), %s)},\n'%(tag, tag, class_name, func, False))


            last_line = line
    return new_file_content

# m = hashlib.md5()

# m.update("lie".encode("utf-8"))
# m.update("n".encode("utf-8"))
# print(m.hexdigest())

files = get_api_files()

with open('../../table_mbuild.py', 'w', encoding='UTF-8') as f:
    f.write("from engine.F3F4.base_structure import cell_item\r\n\r\n")
    for file in files:
        f.write("table_" + file[:-3] + "_tag = \\\n{\n"+create_from_file(file) + '}') 
        f.write("\r\n\r\n")