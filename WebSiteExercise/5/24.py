def print_mat(M: list[list[int]]) -> None:
    if not M:
        print()
    for i in M:
        for j in i:
            print(i, end=" ")
        print()