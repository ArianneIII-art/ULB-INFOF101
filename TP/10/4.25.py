def produit_matriciel(A,B):
    if len(B) != len(A[0]):
        return
    else:
        n = len(B)

    i_max = len(A)
    j_max = len(B[0])
    C = []
    for i in range(i_max):
        C.append([0 for i in range(j_max)])
        for j in range(j_max):
            somme = 0
            for k in range(n):
                somme += A[i][k] * B[k][j]
            C[i][j] = somme
    return C

A = [
        [1,0],
        [2,1],
        [3,2],
    ]

B = [
        [1,2,3],
        [4,5,6],
    ]

for i in produit_matriciel(A,B):
    for j in i:
        print(j,end="\t")
    print()
