
# This file was *autogenerated* from the file stage2.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_12827136631950660209216359962655539318636877290716821157529934201187219916291097512646340799814928196320503957951369709433553128222068986394496491383172957 = Integer(12827136631950660209216359962655539318636877290716821157529934201187219916291097512646340799814928196320503957951369709433553128222068986394496491383172957); _sage_const_41380349828344668841722013593988154321093099094259357736377736864534670060706791545109606752287504685771188039864996559723310519654574206262666374726529575 = Integer(41380349828344668841722013593988154321093099094259357736377736864534670060706791545109606752287504685771188039864996559723310519654574206262666374726529575); _sage_const_9038337376811138597523510592313164861722600343233504981317555262132010358260176119807566000121093361554267202529233467631393363767071867844509978588374760233 = Integer(9038337376811138597523510592313164861722600343233504981317555262132010358260176119807566000121093361554267202529233467631393363767071867844509978588374760233); _sage_const_4 = Integer(4); _sage_const_2324819542625170348844359780621276807555503871252850096339863557086701529895982915686058495680950841284900600209950521822433876540926171344905286018406959743 = Integer(2324819542625170348844359780621276807555503871252850096339863557086701529895982915686058495680950841284900600209950521822433876540926171344905286018406959743); _sage_const_384991383452695588666216941014720946683784460631264884797727791455132234632438790091275812930469701960771509347594917989067900680524277581738313254612711871 = Integer(384991383452695588666216941014720946683784460631264884797727791455132234632438790091275812930469701960771509347594917989067900680524277581738313254612711871)
p= _sage_const_12827136631950660209216359962655539318636877290716821157529934201187219916291097512646340799814928196320503957951369709433553128222068986394496491383172957 
vs= [(_sage_const_1 , _sage_const_41380349828344668841722013593988154321093099094259357736377736864534670060706791545109606752287504685771188039864996559723310519654574206262666374726529575 ), (_sage_const_2 , _sage_const_384991383452695588666216941014720946683784460631264884797727791455132234632438790091275812930469701960771509347594917989067900680524277581738313254612711871 ), (_sage_const_3 , _sage_const_2324819542625170348844359780621276807555503871252850096339863557086701529895982915686058495680950841284900600209950521822433876540926171344905286018406959743 ), (_sage_const_4 , _sage_const_9038337376811138597523510592313164861722600343233504981317555262132010358260176119807566000121093361554267202529233467631393363767071867844509978588374760233 )]

P = PolynomialRing(GF(p), names=('a', 'b', 'c',)); (a, b, c,) = P._first_ngens(3)

f = [c]
for i in range(_sage_const_5 ):
        f += [a * f[-_sage_const_1 ] + b]

G = []
for i in range(_sage_const_1 , _sage_const_5 ):
	g = _sage_const_0 
	for j in range(_sage_const_6 ):
		g += f[j] * i ** j
	G += [g - vs[i-_sage_const_1 ][_sage_const_1 ]]

B = Ideal(G).groebner_basis()
print(B)



