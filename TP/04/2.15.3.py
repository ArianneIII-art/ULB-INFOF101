n = int(input())

if not(n%2):
    print("erreur")
    exit()

s = ""
for i in range(n//2):
    s += ("X "*i + "O " + "X "*(n-(i+1)*2) + "O " + "X "*i)[:-1] + "\n"

print(s, end="")
print("X "*(n//2) + "O " + "X "*(n//2), end="")
print(s[::-1], end="")