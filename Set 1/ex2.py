def vowels(l):
    cnt = 0
    vocale = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in l:
        if i in vocale:
            cnt += 1
    return cnt

print(vowels("obiect"))