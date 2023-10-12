import math 

a = int(input("Dati a: "))
b = int(input("dati b: "))
c = int(input("dati c: "))

print(str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0")

Delta = b**2 - 4 * a * c

if Delta > 0:
    x1 = (-b + math.sqrt(Delta)) / (2*a)
    x2 = (-b - math.sqrt(Delta)) / (2*a)

    print("x1: " + str(x1))
    print("x2: " + str(x2))
elif Delta == 0:
    x1 = (-b + math.sqrt(Delta)) / (2*a)

    print("x1: " + str(x1))
    print("x2: " + str(x1))
else:
    parteReala = -b / (2*a)
    parteImaginara = math.sqrt(-Delta) / (2*a)

    print("Soluții complexe:")
    print("x1 =", parteReala, "+", parteImaginara, "i")
    print("x2 =", parteReala, "-", parteImaginara, "i")