from socket import *

addr = ('pwnable.kr', 9008)
s = socket()
s.connect(addr)
print(s.recv(2048))

