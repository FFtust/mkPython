#!/usr/bin/python3.7 
# -*- coding: utf-8 -*- 

import re
import os
import sys
import hashlib

def get_hash(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

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
            # get class
            ret = re.match(r'class(.*):', line)
            if ret:
                new_file_content += '\r\n'
                new_file_content += (ret.group(0) + '\r\n')
            
            else:
                ret = re.search(r'(.*)def(.*):', line)
                if ret:
                    func = re.search(r'\s(\w*)\(', line).group(0)[1:-1]
                    tag = get_hash(func)

                    para_s = re.search(r'\((.*)\):', line).group(0)[:-1]
                    para_s = para_s.split(",")
                    for i in range(len(para_s)):
                        if '=' in para_s[i]:
                            para_s[i]  = para_s[i][ :para_s[i].index("=")]
                            if i == len(para_s) -1:
                                para_s[i] += ")"
                    # para = re.search(r'\((.*)\):', line).group(0)[:-1].replace("self,", "").replace("self", "")
                    para = ','.join(para_s).replace("self,", "").replace("self", "")
                    last = re.search(r"__fun_type__:(.*)read", last_line)
                    if last:
                        # print("%s%s%s"%(line, "        ", "get_vlue(\"a1\")"))
                        new_file_content += ("%s%sreturn get_value(\"%s\", %s)\r\n"%(line, "        ", tag, para))
                    else:
                        new_file_content += ("%s%srequest(\"%s\", %s)\r\n"%(line, "        ", tag, para))

            last_line = line
    return new_file_content

files = get_api_files()
for file in files:
    with open('../api_'+file, 'w', encoding='UTF-8') as f:
        f.write("import time\r\nfrom engine.interface import get_value, request\r\n\r\n"+create_from_file(file)) 