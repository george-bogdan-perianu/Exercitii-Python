def cmmdc(*args):
    if len(args) == 0:
        return None
    div = args[0]
    for nr in args[1:]:
        while nr != 0:
            rest = div % nr
            div = nr
            nr = rest
    return div

def drepte_unice(lista_puncte):
    drepte = set()
    numar_puncte = len(lista_puncte)
    for i in range(numar_puncte):
        for j in range(i+1,numar_puncte):
            x1,y1 = lista_puncte[i]
            x2,y2 = lista_puncte[j]
            if x1 == x2 and y1 == y2:
                continue
            a = y2-y1
            b = x1-x2
            c = x2*y1 - x1*y2

            numitor_comun = cmmdc(a, b, c)

            a = a//numitor_comun
            b = b//numitor_comun
            c = c//numitor_comun

            if a < 0 or (a==0 and b<0):
                a,b,c = -a,-b,-c

            drepte.add((a,b,c))

    return list(drepte)


