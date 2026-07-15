def cuvinte(l):
    separator = ", . ; ? ! "
    cnt = 0
    OK = False
    for i in l:
        if i not in separator:
            if OK == False:
                cnt += 1
                OK = True
        else :
            OK = False
    return cnt
print(cuvinte("Salut! Ce faci? ,,, Bine."))