from Crypto.Util.number import GCD
from Crypto.PublicKey import RSA
import sys
from output import *

Product_Tree = [Ns]

while True:
	pre_prod_list = Product_Tree[-1]
	new_prod_list = []
	for i in range(0, len(pre_prod_list)-1, 2):
		new_prod_list += [pre_prod_list[i] * pre_prod_list[i+1]]
	if len(prev_prod_list) & 1:
		new_prod_list += [pre_prod_list[-1]]
	Product_Tree.append(new_prod_list)
	if len(new_prod_list) == 1:
		break

Remainder_Tree = [Product_Tree[-1][0]]

for prod_list in Product_Tree[:-1][::-1]:

	new_remainder_list = []
	for i in range(len(prod_list)):
		new_remainder_list += [remainder_list[i//2] % (prod_list[i]) ** 2]

	Remainder_Tree = new_remainder_list

for i in range(len(remainder_list)):
	N = Ns[i]
	z = remainder_list[i]
	if GCD(N, z // N) != 1:
		p = GCD(N, z // N)
		q = N // p
		print("Found!")
		print(f"N = {N}")
		print(f"p = {p}")
		print(f"q = {q}")
		break

