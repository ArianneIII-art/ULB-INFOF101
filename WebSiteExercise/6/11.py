from math import pi

def bonne_planete(diametre):
    return 4 * pi * (diametre/2) ** 2 >= 1000 * 50

print("Bonne planète" if bonne_planete(float(input())) else "Trop petite")