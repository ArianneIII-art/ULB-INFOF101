def factorielle(n: int) -> int:
    tot = 1
    for i in range(1, n+1):
        tot *= i
    return tot

def catalan(n: int) -> int:
    return int(factorielle(2*n) / (factorielle(n+1) * factorielle(n)))