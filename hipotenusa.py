import math
Cateto_oposto = float(input("Cateto Oposto = "))
Cateto_adjacente =float(input("Cateto Adjacente = "))


hipotenusa = math.sqrt((Cateto_oposto ** 2 + Cateto_adjacente ** 2))
print("Hipotenusa = ", hipotenusa)