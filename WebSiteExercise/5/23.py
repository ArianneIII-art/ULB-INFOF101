def init_mat(m: int, n: int) -> list[list[int]]:
    to_return = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(0)
        to_return.append(temp)
        
    return to_return