from socket import *

string = ''
square, binary = 0, 0
sw = 1
add = 0
calc_bin = 0

addr = ('pwnable.kr', 9008)
s = socket()
s.connect(addr)

s.recv(2048)

# Repeat 100 times
for i in range(100):
    lst = s.recv(20).split()
    N, C = int(lst[0][2:]), int(lst[1][2:])

    for i in range(C):
        square = 2 ** i
        binary = square
        for j in range(square,N-1):
            if(sw % 2 == 1):
                string += str(j-1) + ' '
                binary -= 1
            else:
                binary -= 1

            if(binary == 0):
                sw += 1
                binary = square
        string = string[:-1] + '-'
        sw = 1
    string = string[:-1] + '\n'
    lst = s.recv(200).split('-')
    calc_bin = len(lst)
    for result in range(calc_bin):
        if(lst[result] % 10 == 0):
            pass
        else:
            add += 2 ** (calc_bin - result)
    s.send(str(add) + '\n')
    print(s.recv(1024))

s.close()
