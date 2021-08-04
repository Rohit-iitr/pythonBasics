# def is_list_sorted(samplelist):
#     if samplelist.__len__() == 1 or samplelist.__len__() == 0:
#         return True
#     if int(samplelist[0]) > int(samplelist[1]):
#         return False
#     return(is_list_sorted(samplelist[1:]))


# print(is_list_sorted([1, 2, 0]))

def is_list_sorted(samplelist, index):
    listLen = samplelist.__len__()
    if index == listLen-1 or index == listLen:
        return True
    if int(samplelist[index]) > int(samplelist[index+1]):
        return False
    return(is_list_sorted(samplelist, index+1))


print(is_list_sorted([1, 2, 3], 0))
