# def checkNumber(sampleList, number):
#     listLength = sampleList.__len__()
#     if listLength == 0:
#         return False
#     if int(sampleList[0]) == number:
#         return True
#     return checkNumber(sampleList[1:], number)


# print(checkNumber([1, 2, 3, 4, 5], 6))

# def checkNumber(sampleList, number, index):
#     listLength = sampleList.__len__()
#     if index == listLength:
#         return -1
#     if int(sampleList[index]) == number:
#         return index
#     return checkNumber(sampleList, number, index+1)


# print(checkNumber([2], 5, 0))


def checkNumber(sampleList, number):
    listLength = sampleList.__len__()
    if listLength == 0:
        return -1
    if int(sampleList[0]) == number:
        return 0
    outReturn = checkNumber(sampleList[1:], number)
    if outReturn == -1:
        return -1
    else:
        return outReturn+1


print(checkNumber([1, 2, 3, 4, 5], 5))
