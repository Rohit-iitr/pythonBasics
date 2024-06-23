# def find_last_Index_of_n(sampleList, number):
#     lengthOfList = sampleList.__len__()
#     if lengthOfList == 0:
#         return -1
#     if sampleList[lengthOfList-1] == number:
#         return lengthOfList-1
#     return find_last_Index_of_n(sampleList[0:lengthOfList-1], number)

def find_last_Index_of_n(sampleList, number, index):
    lengthOfList = sampleList.__len__()
    if index == lengthOfList:
        return -1
    find_last_Index_of_n(sampleList, number, index+1)
#     if sampleList[lengthOfList-1] == number:
#         return lengthOfList-1
#     return find_last_Index_of_n(sampleList[0:lengthOfList-1], number)


print(find_last_Index_of_n([1, 4, 4, 3, 5, 6, 7], 4))

##i have made changes in f1 branch