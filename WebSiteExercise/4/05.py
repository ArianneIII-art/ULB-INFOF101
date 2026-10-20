def rendre_monnaie(prix: int, x20: int, x10: int, x5: int, x2: int, x1: int) -> tuple[int] | tuple[None]:
    nombre_billet = [x20, x10, x5, x2, x1]
    valeur_des_billet = [20,10,5,2,1]
    somme=0

    for i in range(len(valeur_des_billet)):
        somme += nombre_billet[i]*valeur_des_billet[i]

    if somme < prix:
        return (None, None, None, None, None)
    elif somme == prix:
        return (0, 0, 0, 0, 0)

    to_return = []
    a_rendre = somme - prix
    for i in range(len(valeur_des_billet)):
        to_return.append(a_rendre // valeur_des_billet[i])
        a_rendre -= a_rendre // valeur_des_billet[i] * valeur_des_billet[i]
    
    return tuple(to_return)