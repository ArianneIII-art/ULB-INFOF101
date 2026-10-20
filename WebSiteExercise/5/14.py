def distance_mots(mot_1, mot_2):
    distance = 0
    
    for i in range(len(mot_1)):
        if mot_1[i] != mot_2[i]:
            distance += 1
    return distance