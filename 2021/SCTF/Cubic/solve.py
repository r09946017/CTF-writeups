from Crypto.Util.number import *
import random
from output import *

def add(P, Q, mod):
    x1, y1 = P
    x2, y2 = Q

    if x2 is None:
        return P
    if x1 is None:
        return Q

    if y1 is None and y2 is None:
        x = x1 * x2 % mod
        y = (x1 + x2) % mod
        return (x, y)

    if y1 is None and y2 is not None:
        x1, y1, x2, y2 = x2, y2, x1, y1

    if y2 is None:
        if (y1 + x2) % mod != 0:
            x = (x1 * x2 + 2) * inverse(y1 + x2, mod) % mod
            y = (x1 + y1 * x2) * inverse(y1 + x2, mod) % mod
            return (x, y)
        elif (x1 - y1 ** 2) % mod != 0:
            x = (x1 * x2 + 2) * inverse(x1 - y1 ** 2, mod) % mod
            return (x, None)
        else:
            return (None, None)
    else:
        if (x1 + x2 + y1 * y2) % mod != 0:
            x = (x1 * x2 + (y1 + y2) * 2) * inverse(x1 + x2 + y1 * y2, mod) % mod
            y = (y1 * x2 + x1 * y2 + 2) * inverse(x1 + x2 + y1 * y2, mod) % mod
            return (x, y)
        elif (y1 * x2 + x1 * y2 + 2) % mod != 0:
            x = (x1 * x2 + (y1 + y2) * 2) * inverse(y1 * x2 + x1 * y2 + 2, mod) % mod
            return (x, None)
        else:
            return (None, None)

def myPower(P, a, mod):
    target = (None, None)
    t = P
    while a > 0:
        if a % 2:
            target = add(target, t, mod)
        t = add(t, t, mod)
        a >>= 1
    return target

finitN = p*q*padding

d = pow(e, -1, (p**2+p+1)*(q**2+q+1)*(padding**2+padding+1))
M = myPower(cipher, d, finitN)
flag = long_to_bytes(M[0]) + long_to_bytes(M[1])
print(flag)

