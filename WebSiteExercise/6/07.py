def even(n: int) -> set[int]:
    if n%2:
        return set(range(0, n-1, 2))
    else:
        return set(range(0, n+1, 2))

def is_prime(n: int)-> bool:
    if n == 1 or n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_numbers(n: int) -> set[int]:
    res = set()
    for i in range(n+1):
        if is_prime(i):
            res.add(i)
    return res

def prime_odd_numbers(numbers: list[int]) -> tuple[set[int]]:
    res = (set(), set())
    for i in numbers:
        if is_prime(i):
            res[0].add(i)
        if i%2 == 1:
            res[1].add(i)

    return res