def placer_pion(couleur, colonne, grille: list[list[str]]):
    for i in range(len(grille)):
        if grille[i][colonne] == 'V':
            grille[i][colonne] = couleur
            return True, grille

    return False, grille