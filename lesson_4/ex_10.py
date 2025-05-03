def series(n):
    if n <= 3:
        return 1
    return series(n - 1) + series(n - 2) + series(n - 3)


print(series(7))
