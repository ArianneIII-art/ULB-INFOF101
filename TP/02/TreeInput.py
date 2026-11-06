x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

if x == y or x == z:
    print(f"Valuer présente plusieur fois : {x}")
elif y == z:
    print(f"Valuer présente plusieur fois : {y}")