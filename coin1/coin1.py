from socket import *

# connect pwnable.kr:9007
addr = ('pwnable.kr', 9007)
s = socket()
s.connect(addr)

# print description
print(s.recv(2048))

# Repeat 100 times
for i in range(100):
    N, C = s.recv(30).split()
    N, C = int(N[2:]), int(C[2:])
    H, L = N-1, 0
    M = (L+H)/2
    string = ' '.join([str(insert) for insert in range(L, M)])

    # Repeat Chances Time
    for j in range(C):
        s.send(string + '\n')
        recv = s.recv(10)

        if(int(recv) % 2 == 0):
            L = M
            M = (L+H)/4
        else:
            H = M+1
            M = (L+H)/2

        string = ' '.join([str(insert) for insert in range(L, M)])

    if(recv == 10):
        s.send(str(int(string)-1) + '\n')
    else:
        s.send(string + '\n')
    print(s.recv(1024))
# Print Flag
print(s.recv(1024))
s.close()
