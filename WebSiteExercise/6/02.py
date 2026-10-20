def calcul_prix(produits: dict, catalogue: dict) -> float:
    tot = 0
    for index in produits:
        print(index)
        tot += catalogue[index] * produits[index]
    
    return tot
