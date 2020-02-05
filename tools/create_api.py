#!/usr/bin/python3.7 
# -*- coding: utf-8 -*- 

import re
import os
import sys

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
                last = re.search(r"__fun_type__:(.*)read", last_line)
                if last:
                    # print("%s%s%s"%(line, "        ", "get_vlue(\"a1\")"))
                    new_file_content += ("%s%sreturn %s\n"%(line, "        ", "get_vlue(\"a1\")"))
                else:
                    new_file_content += ("%s%s%s\n"%(line, "        ", "request(\"a1\")"))

            last_line = line
    return new_file_content

files = get_api_files()
for file in files:
    with open('t_'+file, 'w', encoding='UTF-8') as f:
        f.write("class led():\n"+create_from_file(file)) 