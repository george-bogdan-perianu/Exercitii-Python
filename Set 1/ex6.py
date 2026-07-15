def convert(text):
    rez = ""
    for i in range(len(text)):
       c = text[i]
       if c.isupper():
           if i == 0:
               rez += c.lower()
           else:
               rez += "_" + c.lower()
       else:
           rez += c

    return rez

print(convert("AcestaEsteUnTest"))