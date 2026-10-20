from math import sqrt
a, b = float(input()), float(input())

print("Erreur" if a < 0 or b < 0 else sqrt(a*b))