from socket import *
from re import *

sq, bi, sw, add, calc_bin, lst_n = 0,0,0,0,0,0

addr = ('pwnable.kr', 9008)
s = socket()
s.connect(addr)

s.recv(2048)

# Repeat 100 times
for i in range(100):
    string = ''
    N, C = map(int, findall('\d+', s.recv(50)))

    # Repeat Chance times
    for i in range(C):
        sq = 2 ** i
        bi = sq
        for j in range(sq, N):
            if(sw % 2 == 0):
                string += str(j-1) + ' '
                bi -= 1
            else:
                bi -= 1

            if(bi == 0):
                sw += 1
                bi = sq
        string = string[:-1] + '-'
        sw = 0
    string = string[:-1] + '\n'
    s.send(string)
    recv = findall('\d+', s.recv(100))
    calc_bin = len(recv)
    for result in range(calc_bin):
        if(int(recv[result]) % 10 != 0):
            add += 2 ** result
    s.send(str(add-1) + '\n')
    print(s.recv(100))
    string = ''
    add = 0

print(s.recv(1024))
s.close()
