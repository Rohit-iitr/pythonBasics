n = 10
primeNum = 2
while primeNum <= n:
    flag = True
    i = 2
    while i < primeNum:
        if primeNum % i == 0:
            flag = False
        i += 1
    if flag:
        print(primeNum)
    primeNum += 1
