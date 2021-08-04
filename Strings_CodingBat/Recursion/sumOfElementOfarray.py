def sumOfListElement(sampleList):
    listlength = sampleList.__len__()
    if listlength == 0:
        return
    elif listlength == 1:
        return sampleList[0]
    return sampleList[0]+sumOfListElement(sampleList[1:])


print(sumOfListElement([1, 2, 3, 4, 5]))
