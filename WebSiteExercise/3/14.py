import random
secret = random.randint(0, 100)

for i in range(5):
    rep = int(input())
    if rep == secret:
        print(f"Gagné en {i+1} essai(s) !")
        break
    elif secret < rep:
        print("Trop grand")
    else:
        print("Trop petit")


if rep != secret:
    rep = int(input())
    if rep == secret:
        print("Gagné en 6 essai(s) !")
    else:
        print(f"Perdu ! Le secret était {secret}")