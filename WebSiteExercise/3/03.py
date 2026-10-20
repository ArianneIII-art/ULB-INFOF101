a,b,c = int(input()), int(input()), int(input())

if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print(a**2 + a*b)
else:
    print('Erreur')