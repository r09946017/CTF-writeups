from output import *

M = Matrix(QQ, 9, 9)

for i, param in enumerate(params):
	M[0, i] = 1
	M[1, i] = param[0]
	M[2, i] = param[1]
	M[3+i, i] = p

x = int(p^(0.4))

M[0, 6] = 1 / x
M[1, 7] = x
M[2, 8] = x^2

M = M.LLL()

for i in range(9):
	xx = M[i, 7] // x
	print(xx)
	x3 = M[i, 6]
	if xx^3 == x3:
		print(xx)
