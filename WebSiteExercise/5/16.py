def my_pow(a, b) -> list[float] | None:
    if type(a) != int or type(b) != float:
        return

    to_return = []
    for i in range(a):
        to_return.append(b**i)

    return to_return