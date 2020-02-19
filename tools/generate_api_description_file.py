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
        new_file_content += ("class " + file_name[:-3] + "_c():" + '\r\n')   
        for line in f: 
                ret = re.search(r'(.*)def(.*):', line)
                if ret:
                    temp = line.split('(')
                    temp[1] = "self, " + temp[1]
                    # para = re.search(r'\((.*)\):', line).group(0)[:-1].replace("self,", "").replace("self", "")
                    temp = '('.join(temp)

                    new_file_content += "    " + temp + """        \"\"\"简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        \"\"\"
"""

    return new_file_content

files = get_api_files()
for file in files:
    with open('test/'+ file, 'w', encoding='UTF-8') as f:
        f.write("import time\r\n" + create_from_file(file))