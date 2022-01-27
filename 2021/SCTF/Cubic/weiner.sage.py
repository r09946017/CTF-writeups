for f in (e / n).continued_fraction().convergents()[1:]:
    k, d = f.numerator(), f.denominator()
    phi = ((e * d) - 1) / k
    b = -(n - phi + 1)
    dis_sqrt = sqrt(b * b - 4 * n)
    if dis_sqrt.is_integer():
        p = (-b + dis_sqrt) / 2
        q = (-b - dis_sqrt) / 2
        print(p)
        print(q)
        break
