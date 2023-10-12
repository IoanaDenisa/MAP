vector = []

for i in range(8):
    numar = int(input("Introdu elementul " + str(i + 1) + " al vectorului: "))
    vector.append(numar)

n = len(vector)

for i in range(n):
    for j in range(0, n - i - 1):
        if vector[j] > vector[j + 1]:
            vector[j], vector[j + 1] = vector[j + 1], vector[j]

print("Vectorul sortat este:" + str(vector))

