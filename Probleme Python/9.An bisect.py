An = int(input("Introduceti un an: "))

if (An % 4 == 0 and An % 100 != 0) or (An % 400 == 0):
    print("Anul " + str(An) + " este bisect")
else:
    print("Anul " + str(An) + " nu este bisect")