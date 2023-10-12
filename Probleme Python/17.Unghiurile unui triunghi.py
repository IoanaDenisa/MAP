unghi1 = float(input("Introduceti primul unghi: "))
unghi2 = float(input("Introduceti al doilea unghi: "))
unghi3 = float(input("Introduceti al treilea unghi: "))

if (unghi1 + unghi2 > unghi3) and (unghi1 + unghi3 > unghi2) and (unghi2 + unghi3 > unghi1) and (unghi1 > 0) and (unghi2 > 0) and (unghi3 > 0):
    print("Cele trei unghiuri pot forma un triunghi.")
else:
    print("Cele trei unghiuri nu pot forma un triunghi.")