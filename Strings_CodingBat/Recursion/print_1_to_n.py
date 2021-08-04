def print_1_to_n(n):
    # n = 0
    if n == 0:
        return
    print(n)
    print_1_to_n(n-1)


print_1_to_n(10)
