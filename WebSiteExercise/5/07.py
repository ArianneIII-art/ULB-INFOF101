def plus_grand_bord(w):
    bord = ""
    for i in range(len(w)):
        if w[:i] == w[-i:]:
            bord = w[:i]
    return bord