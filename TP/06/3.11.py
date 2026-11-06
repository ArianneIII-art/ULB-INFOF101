from time import time

def timeit(f, n: int=1000):
    before_time = time()
    for i in range(n):
        f()
    after_time = time()
    return after_time - before_time / n