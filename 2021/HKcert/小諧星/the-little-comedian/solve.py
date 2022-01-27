from Crypto.Util.number import *
from output import *

p = int(p, 16)
y_A = int(y_A, 16)
y_B = int(y_B, 16)
c = int(c, 16)

S_AB = (y_A * y_B) ** 2 % p
pt = c // S_AB
flag = long_to_bytes(pt)
print(flag)

