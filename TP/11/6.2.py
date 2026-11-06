def mots(texte: str)-> list[str]:
    liste = []
    tmp = ""
    for letter in texte:
        if letter.isalpha():
            tmp += letter
        else:
            if tmp:
                liste.append(tmp)
                tmp = ""
    if tmp:
        liste.append(tmp)
    return liste


def abreger(a, b):
    t = mots(a)
    s = ''
    for i in range(len(t)):
        if t[i] in abrev:
            s += abrev[t[i]] + " "
        else:
            s += " " + t[i]
    return s

abrev = {"Chuck": "C.", "Norris": "N.", "l’infini": "inf"}
print(abreger("Chuck Norris a compté deux fois jusqu’à l’infini", abrev))
