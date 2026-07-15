#Ex. 5
a= 2**1024
b=str(a)
print(len(b))

#Ex. 6
def fnc(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

#ex 7
def fnc(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '/':
        return x / y
    elif op == '*':
        return x * y

#ex 8
def palindrome(n):
    text = str(n)
    if text == text[::-1]:
        return True
    else:
        return False

#ex 9
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#ex 10
def fnc(x):
    for i in x:
        print(i)

#ex 11
def fnc(x):
    a = max(x)
    b = min(x)
    c = (a+b)/2
    d = (a*b)**(1/2)
    return c,d

#ex 12
def fnc(x):
    mid = len(x)//2
    return max(x[:mid]), min(x[mid:])

#ex 13
def fnc(l):
    rez = []
    for i in l:
        t = str(i)
        if len(t) % 2 == 0 and t == t[::-1]:
            rez.append(i)
    return rez

#ex 14
def fnc(l):
    val_min = min(l)
    val_max = max(l)
    poz_min = l.index(val_min)
    poz_max = l.index(val_max)
    if poz_min < poz_max:
        return l[poz_min : poz_max + 1]
    else:
        return l[poz_max : poz_min + 1]

#ex 15
def fnc(matrice):
    diag = []
    for i in range (len(matrice)):
        diag.append(matrice[i][i])
    diag.sort(reverse=True)
    return diag
