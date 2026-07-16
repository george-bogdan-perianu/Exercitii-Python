def operatii(a,b):
    intersectie = []
    for i in a:
        if i in b and i not in intersectie:
            intersectie.append(i)

    reuniune = []
    for i in a:
        if i not in reuniune:
            reuniune.append(i)

    for i in b:
        if i not in reuniune:
            reuniune.append(i)

    a_minus_b = []
    for i in a:
        if i not in b and i not in a_minus_b:
            a_minus_b.append(i)

    b_minus_a = []
    for i in b:
        if i not in a and i not in b_minus_a:
            b_minus_a.append(i)

    return (intersectie, reuniune, a_minus_b, b_minus_a)