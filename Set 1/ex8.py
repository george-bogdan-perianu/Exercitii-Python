def polinom(pol, x):
    pol = pol.replace("^", "**")
    pol = pol.replace ("x", "*x")
    return eval(pol)
print(polinom("3x ^ 3 + 5x ^ 2 - 2x - 5", 2))