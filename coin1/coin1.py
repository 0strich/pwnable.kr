import socket

def Re_num(lst):
	for i in range(len(lst)):
		lst[i] = int(lst[i][2:])
	return lst

def Mid(num):
	if(num % 2 == 0): return num / 2
	else: return num / 2 + 1

conn = ('pwnable.kr', 9007)

s = socket.socket()
s.connect(conn)
print(s.recv(2048))

# repeat 100 times
for i in range(100):
	lst = Re_num(s.recv(128).split())
	N, C = lst[0], lst[1]
	start, mid, end = 0, Mid(N), N

	# chances number
	for i in range(C):
		send = ' '.join(str(i) for i in range(start, mid))
		s.send(send + '\n')
		recv = int(s.recv(128))
		if(i == C-2): ex_recv, ex_send = recv, send

		if(recv % 2 == 0):
			start = mid
			mid = Mid(start + end)
		else:
			end = mid - 1
			mid = Mid(start + end)

	if(recv == 0 and send == ''):
		if(ex_recv % 2 == 1): s.send(ex_send + '\n')
		else: s.send(str(int(ex_send)+1) + '\n')
	elif(recv == 9): s.send(send + '\n')
	elif(recv == 10): s.send(str(int(send)+1) + '\n')
	print(s.recv(128))

# Print Falg
print(s.recv(128))
s.close()
