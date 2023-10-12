Zilele_săptămânii = {
    1: "luni",
    2: "marti",
    3: "miercuri",
    4: "joi",
    5: "vineri",
    6: "sambata",
    7: "duminica"
}

numar = int(input("Introduceti un numar de la 1 la 7: "))

if numar >= 1 and numar <= 7:
    ziua_saptamanii = Zilele_săptămânii[numar]

    print("Ziua corespunzătoare numărului " + str(numar) + " este " + str(ziua_saptamanii))
else:
    print("Numărul introdus nu este în intervalul corect.")