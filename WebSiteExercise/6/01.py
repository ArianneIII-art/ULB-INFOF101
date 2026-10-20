def inventaire(offres, objets):
    l = {}
    for i in objets:
        l.update(offres[i])

    return l