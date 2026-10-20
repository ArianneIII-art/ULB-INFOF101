def distance_mots(mot_1, mot_2):
    distance = 0

    if len(mot_1) < len(mot_2):
        for i in range(len(mot_2)-len(mot_1)):
            mot_1 += " "

    if len(mot_1) > len(mot_2):
        for i in range(len(mot_1)-len(mot_2)):
            mot_2 += " "
    
    for c in range(len(mot_1)):
        if mot_1[c] != mot_2[c]:
            distance += 1
    return distance

def correcteur(mot, liste_mots):
    dist = []
    for i in range(len(liste_mots)):
        temp = distance_mots(mot, liste_mots[i])
        dist.append(temp)

    best = 0
    for i, v in enumerate(dist):
        if dist[best] > v:
            best = i
    return liste_mots[best]