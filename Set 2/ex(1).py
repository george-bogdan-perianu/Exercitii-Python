def fibonacci2(num_terms,n):
    rez = [0] * (n - 1) + [1]
    for i in range(num_terms):
        next = sum(rez[-n:])
        rez.append(next)

    return rez

print(fibonacci2(3, 5))