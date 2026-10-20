def soleil_leve(x: int,y: int,z: int) -> bool:
    if x < y:
        return x < z < y
    elif x > y or (x == 0 and y == 0):
        return z > x or z < y
    else:
        return False