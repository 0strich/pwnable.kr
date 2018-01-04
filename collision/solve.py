from pwn import *
from subprocess import *

hasscode = 0x21DD09EC
divide = hasscode/5
remainder = divide+(hasscode%5)

payload = p32(divide)*4
payload += p32(remainder)

call(['/home/col/col',payload])
