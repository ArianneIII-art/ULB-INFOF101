def deux_egaux(a: int, b: int, c: int) -> bool:
    return a == b or a == c or b == c

print(deux_egaux(int(input()), int(input()), int(input())) is True)