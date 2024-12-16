# -*- coding: UTF-8 -*-
import json
import os
import socket
from contextlib import nullcontext
from urllib.parse import urlencode
from urllib.request import urlopen

from geopy import Nominatim
from ipapi import ipapi
from mitmproxy import ctx
import requests

this_ip=""
def request(flow):
    flow.request.headers['User-Agent'] = 'MitmProxy'
    ctx.log.info(str("+========="+flow.request.url))
    domain=flow.request.url.split('/')[2]
    ip_api(domain)

def ip_api(domain):  # 可传IP或域名
    if 'http://' in domain:
        name = domain.replace('http://', '')
    else:
        name = domain.replace('https://', '')
    try:
        info = socket.getaddrinfo(name, socket.SOL_TCP)
        # print("============"+domain+"========"+info[0][4][0])
        for addr in info:
            ip = addr[4][0]
            ip_138(ip)
            # ip_geopy(ip)
            print("============"+domain+"========"+str(addr) )


    except socket.gaierror as err:
        print(err)


def ip_138(ip):  # 只能传IP
    dict = {'ip': ip, 'datatype': 'json'}
    params = urlencode(dict)  # 字典转字符串
    url = 'http://api.ip138.com/query/?' + params
    headers = {"token": "0c13402b73625119a32cd2eba79b89d9"}
    rb = requests.get(url, headers=headers)
    response = rb.text
    print(response)

def ip_geopy(ip):
    print(ip)
    location = ipapi.location(ip)
    print(location)