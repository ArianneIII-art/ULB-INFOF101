def soleil_leve_one_star(x: int,y: int,z: int) -> bool:
    if x < y:
        return x <= z < y
    elif x > y or (x == 0 and y == 0):
        return z >= x or z < y
    else:
        return False

def soleil_leve():
    w, x, y, z = int(input()), int(input()), int(input()), int(input())

    for i in range(24):
        if soleil_leve_one_star(w,x, i) or soleil_leve_one_star(y, z, i):
            print(i)
        else:
            print(f'{i} *')

soleil_leve()