def barcketNumbers(S):
    tempStack=list()
    numbers=list()
    positionList=list()
    chrIndex=0
    for chr in S:
        if chr == '(':
            chrIndex+=1
            tempStack.append(chr)
            numbers.append(chrIndex)
            positionList.append(chrIndex)
        elif chr == ')':
            tempStack.pop()
            indexPop=numbers.pop()
            positionList.append(indexPop)
    return positionList



    #         if chrIndex==1:
    #             tempStack.append(chr)
    #             numbers.append(chrIndex)
    #         else:
    #             if tempStack.pop()==')':
    #                 chrIndex-=1
    #                 numbers.append(chrIndex)
    #             else:
    #                 tempStack.append(chr)
    #                 numbers.append(chrIndex)

    # return numbers

print(barcketNumbers('(((()('))




