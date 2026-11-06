def extraire_mots_uniques(texte: str)-> set[str]:
    sett = set()
    tmp = ""
    for letter in texte:
        if letter.isalpha():
            tmp += letter
        else:
            if tmp:
                sett.add(tmp)
                tmp = ""
    if tmp:
        sett.add(tmp)
    return sett


print(
extraire_mots_uniques("Hello wolrd! the cat is here to kille you\n but i think you'll be fine\t d")
)
