def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_prime(lista):
    rez = []
    for i in lista:
        if prime(i):
         rez.append(i)

    return rez