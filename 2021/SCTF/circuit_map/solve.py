from block_cipher import encrypt_data, decrypt_data, encrypt, decrypt
# from public_data import g_tables
from test_data import g_tables
from collections import Counter
import itertools
import ast
import hashlib
import json

key1_lookup = {}

for key1 in range(2**24):
	encrypted = encrypt_data(0, key1)
	if encrypted in key1_lookup: 
		key1_lookup[encrypted].append(key1)
	else:
		key1_lookup[encrypted] = [key1]

print("key1 lookup table created")

def gen_key2_lookup(cts):
	lookups = (dict(), dict(), dict())
	for key2 in range(2**24):
		for ind, ct in enumerate(cts):
			encrypted = decrypt_data(ct, key2)
			d = lookups[ind]
			if encrypted in d:
				d[encrypted].append(key2)
			else:
				d[encrypted] = [key2]
	return lookups

def verify_keys(g_tables, keya_0, keya_1, keyb_0, keyb_1, order):
	iters = itertools.product(keya_0, keya_1, keyb_0, keyb_1)
	new_keys = []
	for key00, key01, key10, key11 in iters:
		t = []
		t.append((key00, key10))
		t.append((key00, key11))
		t.append((key01, key10))
		t.append((key01, key11))
		res = []
		vals = []
		for ind, j in enumerate(order):
			res.append(decrypt(g_tables[j][0], t[ind][0], t[ind][1]))
			vals.append(decrypt(g_tables[j][1], t[ind][0], t[ind][1]))
		if list(set(vals)) != [0]:
			print("Messed Up(Again!), are you drunk?!!!", vals)
		if 3 not in Counter(res).values():
			continue
		new_keys.append((key00, key01, key10, key11))
	return new_keys

inputs = []
# for gate in (5, 6):
gate = 5

gi_tables = g_tables[gate]
validations = [i for _, i in gi_tables]

key2_lookups = gen_key2_lookup(validations[1:])

print("key2 lookups created")
keys = []
for key2_0 in range(2**24):
	if key2_0 % 2**16 == 0:
		print("key2_0 = {}".format(hex(key2_0)[2:]))
		print("nvals = {}".format(len(keys)))
	validation = validations[0]
	encrypted = decrypt_data(validation, key2_0)
	if encrypted not in key1_lookup:
		continue
	poss_key1_0 = key1_lookup[encrypted]
	c1 = encrypted
	for ind in range(1, 4):
		validation = validations[ind]
		encrypted = decrypt_data(validation, key2_0)
		if encrypted in key1_lookup:
			c2 = encrypted
			poss_key1_1 = key1_lookup[encrypted]
			rem_ind = [i for i in range(1, 4) if i != ind]
			if c1 in key2_lookups[rem_ind[0] - 1] \
				and c2 in key2_lookups[rem_ind[1] - 1]:
					i1 = rem_ind[0]
					i2 = rem_ind[1]
			elif c2 in key2_lookups[rem_ind[0] - 1] \
				and c1 in key2_lookups[rem_ind[1] - 1]:
					i2 = rem_ind[0]
					i1 = rem_ind[1]
			else:
				continue
			poss_key2_1_1 = key2_lookups[i1 - 1][c1]
			poss_key2_1_2 = key2_lookups[i2 - 1][c2]
			poss_key2_1 = set(poss_key2_1_1).intersection(set(poss_key2_1_2))
			if len(poss_key2_1) > 0:
				poss_key2_1 = list(poss_key2_1)
				order = [0, i1, ind, i2]
				new_keys = verify_keys(gi_tables, poss_key1_0, poss_key1_1, [key2_0], poss_key2_1, order)
				print("len(new_keys) =", len(new_keys))
				print(new_keys)
				keys.extend(new_keys)
				break
assert len(keys) == 1
inputs.append(keys[0][:2])
inputs.append(keys[0][2:])

print("gate {} inputs = {}".format(gate, inputs))
