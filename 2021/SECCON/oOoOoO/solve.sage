from pwn import *
from Crypto.Util.number import *

def conn():

	r = remote("oooooo.quals.seccon.jp", 8000)
	return r

def solve(r):

	r.recvuntil("M = ")
	M = int(r.recvline().decode().strip())
	r.recvuntil("S = ")
	S = int(r.recvline().decode().strip())
	for i in range(128):
    		S -= 79 * (256 ** i)
	S %= M

	a = [(32 * (256 ** i)) % M for i in range(128)]

	n = len(a)
	N = ceil(sqrt(n) / 2)

	b = []
	for i in range(n):
    		vec = [0 for _ in range(n + 1)]
    		vec[i] = 1
    		vec[-1] = N * a[i]
    		b.append(vec)

	b.append([1 / 2 for _ in range(n)] + [N * S])
	b.append([0 for _ in range(n)] + [M])

	BB = matrix(QQ, b)
	BB = BB.LLL()

	for e in BB:
		if e[-1] == 0:
			msg = 0
			isValidMsg = True
			for i in range(len(e) - 1):
				ei = 1 - (e[i] + (1 / 2))
				if ei != 1 and ei != 0:
					isValidMsg = False
					break

				msg += (79 + 32 * int(ei)) * (256 ** i)

			if isValidMsg:
				r.sendline(long_to_bytes(msg))

r = conn()
solve(r)
r.interactive()
