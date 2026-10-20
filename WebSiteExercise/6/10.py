def insertion_sort(tab):
    for i in range (1, len(tab)):
        c = i-1
        temp = tab[i]
        tab.pop(i)
        while c >= 0 and temp[0] < tab[c][0]:
            c -= 1
        tab.insert(c+1, temp)
    return tab


def valeurs(dico: dict) -> list[str]:
    liste = []
    for i in dico:
        liste.append((i, dico[i]))

    liste = insertion_sort(liste)

    to_return = []
    for i in liste:
        to_return.append(i[1])

    return  to_return