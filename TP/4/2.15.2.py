n = int(input())

if not(n%2):
    print("erreur")
    exit()

for i in range(n//2):
    print("X "*i + "O " + "X "*(n-(i+1)*2) + "O " + "X "*i)

print("X "*(n//2) + "O " + "X "*(n//2))

for i in range(n//2-1, -1, -1):
    print("X "*i + "O " + "X "*(n-(i+1)*2) + "O " + "X "*i)