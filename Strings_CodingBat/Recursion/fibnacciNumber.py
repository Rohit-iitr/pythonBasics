def fibnacciSeries(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = fibnacciSeries(n-1)
    b = fibnacciSeries(n-2)
    return a+b


print(fibnacciSeries(9))
