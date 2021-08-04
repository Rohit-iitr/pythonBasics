def reverList(sampleList, index):
    lenList = len(sampleList)
    if index == lenList:
        return
    reverList(sampleList, index+1)
    print(sampleList[index])


reverList([1, 2, 3, 4, 5, 6], 0)
