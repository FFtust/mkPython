#!/usr/bin/python3.7 
# -*- coding: utf-8 -*- 

import re
import os
import sys
import hashlib

API_DIR = "../device/api"

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
            ret = re.search(r'(.*)def(.*):', line)
            if ret:
                # func = line.split('(')[0]
                func = re.search(r'\s(\w*)\(', line).group(0)[1:-1]
                m = hashlib.md5()
                m.update(func.encode("utf-8"))
                tag = m.hexdigest()
                new_file_content += ('"%s": {"key":None, "obj":cell_item("%s", "%s", (), %s)},\n'%(tag, tag, func, False))


            last_line = line
    return new_file_content

# m = hashlib.md5()

# m.update("lie".encode("utf-8"))
# m.update("n".encode("utf-8"))
# print(m.hexdigest())

files = get_api_files()
for file in files:
    with open('../table_'+file, 'w', encoding='UTF-8') as f:

        f.write("from engine.base_structure import cell_item\r\n\r\n"+"table_halocode_tag = \\\n{\n"+create_from_file(file) + '}') 
        create_from_file(file)

# table_halocode_tag = \
# {
#     "T1": {"key":1, "obj":cell_item("T1", "halo.button.is_pressed", (), False)},
#     "T2": {"key":2, "obj":cell_item("T2", "led.show_all", (0,0,0), None)},
# }
