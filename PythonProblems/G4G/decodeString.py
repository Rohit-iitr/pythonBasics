def decodedString(s):
    tempStack = []
    popedPower = ''
    numbericStr = '0123456789'
    alphaStr = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for item in s:
        tempStack.append(item)
        if item == ']':
            tempStr = ''
            popFlag = True
            while popFlag:
                popedItem = tempStack.pop()
                if popedItem == ']':
                    pass
                elif popedItem == '[':
                    popFlag = False
                    popedPowerFlag = True
                    popStr = ''
                    popedPower = ''
                    while popedPowerFlag and (tempStack.__len__() > 0):
                        popedPower = tempStack.pop()
                        if popedPower == '[' or popedPower == ']' or (alphaStr.find(popedPower[0]) >= 0):
                            popedPowerFlag = False
                            tempStack.append(popedPower)
                        elif numbericStr.find(popedPower) >= 0:
                            popStr = popedPower+popStr

                else:
                    tempStr = popedItem+tempStr
            tempStr = tempStr*int(popStr)
            tempStack.append(tempStr)
    return tempStack.pop()


print(decodedString('11[geeks]'))
