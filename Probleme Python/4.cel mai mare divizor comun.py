Numar1 = int(input("Introduceti primul numar: "))
Numar2 = int(input("Introduceti al doilea numar: "))

while Numar1 != Numar2:
    if Numar1 > Numar2:
        Numar1 = Numar1 - Numar2
    else:
        Numar2 = Numar2 - Numar1

print("Cel mai mare divizor comun este: " + str(Numar1))