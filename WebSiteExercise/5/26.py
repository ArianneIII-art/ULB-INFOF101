def antisymetrique(M: list[list[int]]) -> bool:
    for i, liste in enumerate(M):
        for j, elem in enumerate(liste):
            if M[i][j] != -M[j][i]:
                return False
    
    return True