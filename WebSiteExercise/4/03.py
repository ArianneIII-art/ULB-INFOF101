def premier(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

x = int(input())

for i in range(2, x):
    if premier(i):
        print(i)