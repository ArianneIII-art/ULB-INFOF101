def factorielle(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res

def valeur_absolue(x):
    return x if x > 0 else -x

x = float(input())

res = x


i = 3
terme = (x**i)/factorielle(i)

while valeur_absolue(terme) > 10**-6:
    res -= terme
    i += 2
    terme = (x**i)/factorielle(i)
    res += terme
    i += 2
    terme = (x**i)/factorielle(i)

print(res)