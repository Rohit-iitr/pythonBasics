def xtoPowern(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a*xtoPowern(a, b-1)
    else:
        return (1/a)*xtoPowern(a, b+1)


print(xtoPowern(4, 0))
