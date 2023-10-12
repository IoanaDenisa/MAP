numere = []
n = int(input("Câte numere dorești să introduci? "))

for i in range(n):
    numar = float(input(f"Introdu numărul {i + 1}: "))
    numere.append(numar)

minim = min(numere)
maxim = max(numere)

print(f"Cel mai mic număr este: {minim}")
print(f"Cel mai mare număr este: {maxim}")