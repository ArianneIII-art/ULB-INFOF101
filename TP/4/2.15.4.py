n = int(input())

if not(n%2):
    print("erreur")
    exit()

for i in range(n):
    for j in range(n):
        if i == j or i+j == n-1:
            print("O", end=" ")
        else:
            print("X", end=" ")
    print()