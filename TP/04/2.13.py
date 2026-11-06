n = int(input("Entrez un nombre entier : "))

resultat = 1
for i in range(2, n+1):
    resultat *= i

print(f"La factorielle de {n} est {resultat}")