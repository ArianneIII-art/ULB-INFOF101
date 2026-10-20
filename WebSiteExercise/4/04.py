import random

def alea_dice(s: int) -> bool:
    random.seed(s)
    dice = {random.randint(1,6),random.randint(1,6),random.randint(1,6)}
    return {1,2,4} == dice