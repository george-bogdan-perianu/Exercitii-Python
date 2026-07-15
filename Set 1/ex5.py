def fnc(a):
    speciale = "\r\t\n\a\b\f\v"
    for c in speciale:
        if c in a:
            return True
    return False

print(fnc("Text simplu"))
print(fnc("Aici avem un tab\tsi un enter\n"))