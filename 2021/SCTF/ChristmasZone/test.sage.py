
# This file was *autogenerated* from the file test.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_6 = Integer(6); _sage_const_512 = Integer(512)
from random import randint

def gen():
    a,b,x = seed
    while _sage_const_1 :
        x = (a*x + b) % p
        yield x

p = random_prime(_sage_const_1 <<_sage_const_512 )
seed = [randint(_sage_const_2 , p-_sage_const_1 ) for _ in range(_sage_const_3 )]

def Function_function():
    f=_sage_const_0 
    g = gen()
    for e in range(_sage_const_6 ):
        print(next(g))
    return

for i in range(_sage_const_3 ):
	Function_function()

