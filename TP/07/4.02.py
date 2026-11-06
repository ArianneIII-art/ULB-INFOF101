def sont_tous_impairs(liste: list[int])-> bool:
    for i in liste:
        if i % 2 == 0:
            return False
    return True
