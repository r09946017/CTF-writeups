import itertools

def small_roots(f, bounds, m=1, d=None):
	if not d:
		d = f.degree()

	R = f.base_ring()
	N = R.cardinality()
	
	f /= f.coefficients().pop(0)
	f = f.change_ring(ZZ)

	G = Sequence([], f.parent())
	for i in range(m+1):
		base = N^(m-i) * f^i
		for shifts in itertools.product(range(d), repeat=f.nvariables()):
			g = base * prod(map(power, f.variables(), shifts))
			G.append(g)

	B, monomials = G.coefficient_matrix()
	monomials = vector(monomials)

	factors = [monomial(*bounds) for monomial in monomials]
	for i, factor in enumerate(factors):
		B.rescale_col(i, factor)

	B = B.dense_matrix().LLL()

	B = B.change_ring(QQ)
	for i, factor in enumerate(factors):
		B.rescale_col(i, 1/factor)

	H = Sequence([], f.parent().change_ring(QQ))
	for h in filter(None, B*monomials):
		H.append(h)
		I = H.ideal()
		if I.dimension() == -1:
			H.pop()
		elif I.dimension() == 0:
			roots = []
			for root in I.variety(ring=ZZ):
				root = tuple(R(root[var]) for var in f.variables())
				roots.append(root)
			return roots

	return []

bounds = (2^400, 2^512)

n = 64392795853847475796939596948374573513341136006013188358665448316305707477998438325517993586430100318003625505157712138814030987620038360820900112359350226402638642419396935215229157012026467896203963294845355310085476165076942465877433408205263068546705226319393063008332679430070032638523530045872344446063
e = 2122057207992053205813770227849040233008910764365408170807753866052370273036652511326089337097360978735074872616654616913246201310148862001548717525315340025551386286859760434183016041810428435636703565295076056164899655565064479034568939414539781862057507880933035055798925469493379171063624396109774778347319852379080566673380010455470481679145108944783447900704049011034802113265281840271722439782048757303053321402550218515376334799866137565004833177407151305907248656027100625115285653505268015889011758846754314363803434935375750532978323034293333866829909394024977100845590141939498841156488858312084500963993

R = Integers(e)
P.<k, p_plus_q> = PolynomialRing(R)
f = k * (n^2 - n + 1 + (n+1) * p_plus_q + p_plus_q^2) + 1

print(small_roots(f, bounds, m=3, d=4))


