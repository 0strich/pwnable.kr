from socket import *
from re import *

bi, sq, sw, num = 0,0,0,0
lt_send = 0

addr = ('pwnable.kr', 9008)
s = socket()
s.connect(addr)
s.recv(2048)

# Repeat 100 times
for i in range(100):
    string = ''
    init = s.recv(50).decode('utf-8').split()
    N, C = int(findall('\d+', init[0])[0]), int(findall('\d+', init[1])[0])

    # Repeat Chance times
    for j in range(C):
        sq = 2 ** j
        bi = sq

        # Repeat Coin number times
        for z in range(bi, N):
            if(sw % 2 == 0):
                string += str(z) + ' '
                bi -= 1
            else:
                bi -= 1
            if(bi == 0):
                sw += 1
                bi = sq
        string = string[:-1] + '-'
        sw = 0

    string = ((string[:-1]) + '\n').encode('utf-8')
    s.send(string)
    recv = s.recv(100).decode('utf-8').split('-')
    # Second Sending Coin
    num = len(recv)
    for last in range(num):
        if(int(recv[last]) % 10 != 0):
           lt_send += 2 ** last
    s.send((str(lt_send) + '\n').encode('utf-8'))
    print(s.recv(100).decode('utf-8'))
    string = ''
    lt_send = 0

# Print Flag
print(s.recv(1024).decode('utf-8'))

# cancle socket connect
s.close()
