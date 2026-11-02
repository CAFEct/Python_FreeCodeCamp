def fibonacci(n):
    sequence = [0,1]

    if n <= 1:
        return n

    a,b = 0, 1
    for _ in range(a, n + 1):
        a,b = b, a + b
    return b
