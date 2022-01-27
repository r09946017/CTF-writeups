"""
once you've found the input labels which make the circuit return `true`,
then concatenate them together, hash them,
and xor with the provided string to obtain the flag
"""

import hashlib
import json

from yao import evaluate_circuit
from public_data import g_tables

from Crypto.Util.number import *
import itertools

def xor(A, B):
    return bytes(a ^ b for a, b in zip(A, B))


##########################################################


circuit_filename = "circuit.json"
with open(circuit_filename) as json_file:
    circuit = json.load(json_file)

inputs = [
	(13675268, 8343801),
	(12870274, 10251687),
	(12490757, 6827786),
	(2096572, 3391233)
]

indices = [1,2,3,4,5,6,7,9]
keys = {
	1: [],
	2: [],
	3: [],
	4: [],
	5: [],
	6: [],
	7: [],
	9: []
}
for i, j, k, l in itertools.product(*inputs):
	_ = {
		1: i,
		2: j,
		3: k,
		4: l
	}
	evaluation = evaluate_circuit(circuit, g_tables, _)
	for ind in indices:
		if evaluation[ind] not in keys[ind]:
			keys[ind] += [evaluation[ind]]

##########################################################

the_chaos = b""
for i in keys:
	tmp = sum(keys[i])
	the_chaos += bytes(long_to_bytes(tmp))
mask = hashlib.md5(the_chaos).digest()
enc = bytes.fromhex("1661fe85c7b01b3db1d432ad3c5ac83a")
flag = xor(mask, enc)
print(flag)

