from Crypto.Util import Counter
from Crypto.Cipher import AES
from Crypto.Util.number import *
import os
import random
from output import *

def XOR(a, b):
        return bytes(aa ^ bb for aa, bb in zip(a, b))

def bytes_to_Matrix(bs):
	vec = []
	for b in bs:
		for i in range(7, -1, -1):
			if b & (1 << i):
				vec += [1]
			else:
				vec += [0]
	return vec

plaintext = b"Congratulations! hkcert21{"
ciphertext = bytes.fromhex(ciphertext)
Goal = XOR(plaintext, ciphertext[:26])
b = bytes_to_Matrix(Goal)
A = []
candidate = []

for k in range(256):
	key = int.to_bytes(k, 1, "big") + b"\0" * 15
	aes128 = AES.new(key = key, mode = AES.MODE_CTR, counter = Counter.new(128, initial_value=0))
	text = os.urandom(62)
	_ = XOR(text, aes128.encrypt(text))
	candidate += [_]
	A += [bytes_to_Matrix(_[:26])]
	
print("A = {}".format(A))
print("b = {}".format(b))