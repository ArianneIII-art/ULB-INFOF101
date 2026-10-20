x = int(input())

for i in range(x):
    print(" "*(x-i-1), end="")
    for c in range(i+1, i*2+2):
        print(c%10,end="")
    for c in range(i*2, i, -1):
        print(c%10,end="")
    print()