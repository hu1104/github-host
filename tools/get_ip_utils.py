'''
Author: zongxing
Date: 2021-12-02 11:28:27
LastEditTime: 2021-12-02 12:44:08
LastEditors: zongxing
FilePath: \github-host-master\tools\get_ip_utils.py
'''
import requests
from bs4 import BeautifulSoup
import re,json


# def getIpFromIpaddress(site):
#     headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36',
#                'Host': 'ipaddress.com'}
#     url = "https://ipaddress.com/search/" + site
#     trueip = None
#     try:
#         res = requests.get(url, headers=headers, timeout=5)
#         soup = BeautifulSoup(res.text, 'html.parser')
#         ip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", res.text)
#         result = soup.find_all('div', class_="comma-separated")
#         for c in result:
#             if len(ip) != 0:
#                 trueip = ip[0]
#     except Exception as e:
#         print("查询" + site + " 时出现错误: " + str(e))
#     return trueip


def getIpFromIpaddress(site):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36',
               'Host': 'websites.ipaddress.com'}
    url = "https://websites.ipaddress.com/" + site
    trueips = []
    try:
        res = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        # ip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", res.text)
        # print(ip)
        result = soup.find_all('table', class_="panel-item table table-stripes table-v")
        # print(result)
        for c in result:
            # print(type(c))
            if "IPv4 Addresses" in c.strings:
                # print(c)
                contents = c.find_all('ul', class_="comma-separated")[0].find_all("li")
                for content in contents:
                    trueip = content.string
                    print(trueip)
                    trueips.append(trueip)

                # print(content.string)
    except Exception as e:
        print("查询" + site + " 时出现错误: " + str(e))
    return trueips


def getIpFromChinaz(site):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36',
               'Host': 'ip.tool.chinaz.com'}
    url = "http://ip.tool.chinaz.com/" + site
    trueip = None
    try:
        res = requests.get(url, headers=headers,timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        result = soup.find_all('span', class_="Whwtdhalf w15-0")
        for c in result:
            ip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", c.text)
            if len(ip) != 0:
                trueip = ip[0]
    except Exception as e:
        print("查询" + site + " 时出现错误: " + str(e))
    return trueip


def getIpFromWhatismyipaddress(site):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36',
               'Host': 'ip.tool.chinaz.com'}
    url = "https://whatismyipaddress.com//hostname-ip"
    data = {
        "DOMAINNAME": site,
        "Lookup IP Address": "Lookup IP Address"
    }
    trueip = None
    try:
        res = requests.post(url, headers=headers, data=data,timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        result = soup.find_all('span', class_="Whwtdhalf w15-0")
        for c in result:
            ip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", c.text)
            if len(ip) != 0:
                trueip = ip[0]
    except Exception as e:
        print("查询" + site + " 时出现错误: " + str(e))
    return trueip

def getIpFromipapi(site):
    '''
    return trueip: None or ip
    '''
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36',
               'Host': 'ip-api.com'}
    url = "http://ip-api.com/json/%s?lang=zh-CN" % (site)
    trueip = None
    try:
        res = requests.get(url, headers=headers,timeout=5)
        res=json.loads(res.text)
        if(res["status"]=="success"):
            trueip=res["query"]
    except Exception as e:
        print("查询" + site + " 时出现错误: " + str(e))
    return trueip