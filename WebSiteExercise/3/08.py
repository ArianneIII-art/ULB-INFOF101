letter, a = input(), float(input())

if letter == "T":
    print(2**0.5/12*a**3)
elif letter == "C":
    print(a**3)
elif letter == "O":
    print(2**0.5/3*a**3)
elif letter == "D":
    print((15+7*5**0.5)/4*a**3)
elif letter == "I":
    print(5*(3+5**0.5)/12*a**3)
else:
    print("Polyèdre non connu")