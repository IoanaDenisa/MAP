n = int(input("Câte numere se afla in lista: "))
numere = []

for i in range(n):
    numar = float(input("Introdu numărul " + str(i + 1) + ": "))
    numere.append(numar)

suma = sum(numere)

media = suma / n if n > 0 else 0

print("Suma numerelor este: " + str(suma))
print("Media numerelor este: " + str(media))