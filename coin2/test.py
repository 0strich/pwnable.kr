from socket import *
from re import *

addr = ('pwnable.kr', 9008)
s = socket()
s.connect(addr)
s.recv(2048)

string = findall('\d+', s.recv(40))
print(type(string))
