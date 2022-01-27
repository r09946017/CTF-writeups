from pwn import *

def conn():

	c = remote("chalp.hkcert21.pwnable.hk", 28157)
	return c

def get_one(c):
	
	c.sendline(b"pkey")
	c.sendline(b"backup")
	c.recvuntil(b"0x")
	r = int(c.recvline().strip(), 16)

	c.sendline(b"send 12d597c58eeee503")
	c.recvuntil(b"0x")
	N = int(c.recvline().strip(), 16)
	N = 1357157737484444931 ** 17 - N
	for i in range(2, 133):
		while N % i == 0:
			N //= i
			print(i)
	return N, r
	
c = conn()
Ns, rs = [], []
for _ in range(5):
	N, r = get_one(c)
	Ns += [N]
	rs += [r]
print("Ns = {}".format(Ns))
print("rs = {}".format(rs))
'''
_ = crt(rs, Ns)
secret = int(_ ^ (1/17))
assert secret ^ 17 == _
print(secret)
'''
c.sendline(b"flag")
c.interactive()

