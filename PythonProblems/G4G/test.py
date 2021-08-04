num = 49901999

if num > 0:
    evenSum = 0
    oddSum = 0
    while num > 0:
        remin = num % 10
        if remin % 2 == 0:
            evenSum = evenSum+int(remin)
        else:
            oddSum = oddSum+int(remin)
        num = num//10
    print(evenSum, " ", oddSum)
else:
    print('0', " ", "0")


def reverse(n):
    # Implement Your Code Here
    initNum = n
    if n > 0:
        reversedNumber = ''
        while n % 10 == 0:
            n = n/10
        while n >= 1:
            reminder = n % 10
            reversedNumber = reversedNumber+str(int(reminder))
            n = n/10
        if initNum == int(reversedNumber):
            return True
        else:
            return False
    else:
        return False


print(reverse(000))
a = 0
b = 0
while b:
    print('b is something')


def tae():
    return 3, 4


a, b = tae()
print(a)
print(b)

exit()
a = 10
a += 2
print(a)
a = +2
print(a)

a = 2
sum = 0
index = 0
while index <= a:
    sum = sum+index
    index += 2
print(sum)


listOfN = [1, 2, 3, 4]
print(listOfN[-2:])


sampleList = list()
print(sampleList.__len__())


def func(num):
    return func(num-1)


num = 5
ans = func(num-1)
print(ans)


# listTest = [1, 2, 3]
# listTest.insert(0, 0)
# listTest.insert(0, 90)
# ab = []
# ab.append('rohit')
# testStr = 'roht'+'rohit'
# for item in testStr:
#     print(item)
# print(ab)

# print('ab'*3)

# while not listTest:
#     print(listTest.pop)

# print(listTest)

# for x in range(9):
#     print(x)
