def fib(x):
    if x <= 2:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


cache = {}
def fib_cached(x):
    global cache
    if x in cache:
        return cache[x]
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        val = fib(x - 1) + fib(x - 2)
        cache[x] = val
        return val


if __name__ == '__main__':
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(6) == 8
    print("Tests passed")