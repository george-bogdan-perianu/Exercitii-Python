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

print(cmmdc(24, 36, 48))
print(cmmdc(100, 75, 50, 25))
