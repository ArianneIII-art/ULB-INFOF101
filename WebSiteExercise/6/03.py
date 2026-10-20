def tris(tab):
    for i in range (1, len(tab)):
        c = i-1
        temp = tab[i]
        tab.pop(i)
        while (c >= 0) and (temp[1] < tab[c][1]):
            c -= 1
        tab.insert(c+1, temp)
    return tab

def top_3_candidats(moyennes):
    l = []
    for i in moyennes:
        l.append((i, moyennes[i]))
    l = tris(l)

    return l[-1][0], l[-2][0], l[-3][0]

print(
    top_3_candidats({'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
                 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
                 'Candidat 4': 33})

)