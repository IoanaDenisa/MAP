Numar = int(input("Introduceti un numar: "))
factorial = 1

if Numar < 0:
    print("Nu exista factorial pentru numere negative")
elif Numar == 0:
    print("Factorialul numarului " + str(Numar) + " este 1")
else:
     for i in range(1,Numar + 1):
          factorial = factorial*i
          print("Factorialul numarului " + str(Numar) + " este " + str(factorial))