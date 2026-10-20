from random import randint

def create_map(size, trapsNbr):
    dico = dict()
    dico[(randint(1, size), randint(1, size))] = 1
    
    for i in range(trapsNbr):
        x, y = randint(1, size), randint(1, size)
        while not(dico.get((x, y)) is None):
            x, y = randint(1, size), randint(1, size)
        dico[(x,y)] = -1
    
    return dico

def play_game(map_size, treasure_map):
    continue_game = True
    while continue_game:
        x, y = input().split()

        if not(x.isalnum() and y.isalnum()):
            continue
        else:
            x, y = int(x), int(y)
        
        if x > map_size or y > map_size:
            continue

        if not(treasure_map.get((x, y)) is None):
            return treasure_map[(x,y)] == 1