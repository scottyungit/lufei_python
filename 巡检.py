# coding=utf-8
from telnetlib import Telnet
import sys
import time
ip_file = open("file","r")
ips = ip_file.readlines()
telnet_port = 23
print(ips)
for ip in ips:
    ip = ip.rstrip()
    child = spawn('telnet %s %s' %(ip,telnet_port))
    print(child)
    #tn=Telnet(ip,telnet_port)
    #print(tn)
