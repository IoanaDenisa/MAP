Numar = int(input("Introdu un număr întreg: "))

def numar_prim(Numar):
    if Numar <= 1:
        return False
    if Numar <= 3:
        return True
    if Numar % 2 == 0 or Numar % 3 == 0:
        return False
    i = 5
    while i * i <= Numar:
        if Numar % i == 0 or Numar % (i + 2) == 0:
            return False
        i += 6
    return True

if numar_prim(Numar):
    print(str(Numar) + " este un număr prim.")
else:
    print(str(Numar) + " nu este un număr prim.")