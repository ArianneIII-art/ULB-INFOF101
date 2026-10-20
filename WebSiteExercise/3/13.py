x, tot = int(input()), 0

if x >= 0:
    for i in range(x):
        tot += int(input())
    print(tot)
else:
    x = input()
    while x != 'F':
        tot += int(x)
        x = input()
    print(tot)