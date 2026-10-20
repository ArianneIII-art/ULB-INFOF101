def trace(M: list[list[int]]) -> int:
    res = 0

    for index, element in enumerate(M):
        res += element[index]

    return res