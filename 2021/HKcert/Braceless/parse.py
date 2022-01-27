from math import gcd

with open("transcript.log", "r") as f:
	lines = f.readlines()

Ns = []
rs = []
ps = [1237, 307, 4871, 457]

for _ in range(65537 // 4):
	m1 = int(lines[7 * _ + 4].strip(), 16)
	m2 = int(lines[7 * _ + 6].strip(), 16)
	N = gcd(2 ** 65537 - m1, 3 ** 65537 - m2)
	for i in range(2, 300):
		while N % i == 0:
			N //= i
	for p in ps:
		while N % p == 0:
			N //= p
	Ns += [N]
	if N >= (1 << 1024) or N <= (1 << 1022):
		print(N)
	rs += [int(lines[7 * _ + 8].strip(), 16)]

print("Ns = {}".format(Ns))
print("rs = {}".format(rs))

