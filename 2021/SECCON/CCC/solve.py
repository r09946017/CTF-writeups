from output import *
# from tmp import *
from decimal import *

getcontext().prec = 1000

pb = int(Decimal(23*n) ** (Decimal(1)/Decimal(3))) + 1

for i in range(100000):
	_ = (pb**3) - (23*n) 
	b = int(Decimal(_) ** (Decimal(1)/Decimal(3)))
	
	if (b**3 == _) or ((b+1)**3 == _):
		print("Found!")
		print(f"pb = {pb}")
		print(f"b = {b}")
		break
	pb += 1
	if i % 100 == 0:
		print(i)



