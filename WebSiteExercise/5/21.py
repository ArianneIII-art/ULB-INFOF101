def list_from_two_to_one_level(liste):
    to_return = []
    for i in liste:
        if type(i) == list:
            for c in i:
                if c:
                    to_return.append(c)
        else:
            if i:
                to_return.append(i)
    return to_return


def liste_des_mots(file: str):
    with open(file) as f:
        SPECIAL_CHAR = [ ' ', '\t',  '-',   "'",   '"',  '?',  '!',  ':',  ';',  '.',  ',',  '*',  '=',  '(',  ')',  '1', '2', '3',  '4', '5', '6', '7', '8', '9', '0']
        l = []
        for ligne in f:
            if ligne != '\n':
                if ligne[-1] == '\n':
                    l.append(ligne[:-1].lower())
                else:
                    l.append(ligne.lower())

        for i in SPECIAL_CHAR:
            for c in range(len(l)):
                l[c] = l[c].split(i)
            l = list_from_two_to_one_level(l)

        l = list(set(l))
        l.sort(key=str.lower)
        return l