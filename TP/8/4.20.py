def chiffrer(texte: str, decalage: int)->str:
    while decalage < 0:
        decalage += 26
    while decalage >= 26:
        decalage -= 26
    texte = texte.upper()
    res = ""
    for i in texte:
        tmp = ord(i)
        tmp += decalage
        if tmp > 122:
            tmp -= 26
        res += chr(tmp)
    return res

def dechiffrer(texte: str, decalage: int)-> str:
    while decalage < 0:
        decalage += 26
    while decalage >= 26:
        decalage -= 26
    texte = texte.upper()
    res = ""
    for i in texte:
        tmp = ord(i)
        tmp -= decalage
        if tmp < 0:
            tmp += 26
        res += chr(tmp)
    return res


print(chiffrer("BONJOUR", 3))
print(dechiffrer(chiffrer("BONJOUR", 3), 3))
