import random

def bat_turn(joueur_1: int, joueur_2: int) -> int:
    if  joueur_1 == joueur_2:
        return 0
    elif (joueur_1, joueur_2) in [(0, 2),(1, 0),(2, 1)]:
        return 1
    else:
        return -1

def bat_int_to_str(i: int) -> str:
    return "Pierre" if i == 0 else ("Feuille" if i == 1 else "Ciseaux")

PIERRE = 0
FEUILLE = 1
CISEAUX = 2
POINT = 0

s = int(input())
random.seed(s)

for i in range(5):
    j_move, o_move = int(input()), random.randint(0,2)

    turn = bat_turn(j_move,o_move)
    POINT += turn

    match turn:
        case -1:
            print(f"{bat_int_to_str(o_move)} bat {bat_int_to_str(j_move)} : {POINT}")
        case 0:
            print(f"{bat_int_to_str(o_move)} annule {bat_int_to_str(j_move)} : {POINT}")
        case 1:
            print(f"{bat_int_to_str(o_move)} est battu par {bat_int_to_str(j_move)} : {POINT}")

if POINT > 0:
    print("Gagné")
elif POINT == 0:
    print("Nul")
else:
    print("Perdu")