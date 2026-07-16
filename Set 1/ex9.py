def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

    text += "a"

def cel_mai_mare_prime(text):
    maxim = -1
    numar_curent = ""
    for c in text:
        if c.isdigit():
            numar_curent += c
        else:
            if numar_curent != "":
                numar = int(numar_curent)
                if prime(numar) and numar > maxim:
                    maxim = numar

            numar_curent = ""

    return maxim

print(cel_mai_mare_prime("ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda"))
