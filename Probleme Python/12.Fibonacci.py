numar_antepreantant = 0
numar_antecurent = 1

Numar = int(input("Introduceti un numar: "))

if Numar <= 0:
    print("Nu există numere Fibonacci")
elif Numar == 1:
    print("Primele " + str(Numar) + " numere Fibonacci sunt: ")
    print(numar_antepreantant)
else:
    print("Primele " + str(Numar) + " numere Fibonacci sunt: ")
    print(numar_antepreantant)
    print(numar_antecurent)
    
    for _ in range(2, Numar):
        numar_nou = numar_antepreantant + numar_antecurent
        print(numar_nou)
        numar_antepreantant = numar_antecurent
        numar_antecurent = numar_nou
