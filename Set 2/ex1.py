def fibonacci(n):
    if n<0:
        return []
    if n==0:
        return [0]

    rez = [0,1]
    for i in range(2,n):
        next = rez[-1] + rez[-2]
        rez.append(next)

    return rez

print(fibonacci(10))