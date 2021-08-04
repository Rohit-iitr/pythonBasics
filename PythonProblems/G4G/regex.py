import numpy as np
import re

def ExtractNumber(S):
    #inputStr ='erwrwe'
    inputStr=S
    splitedStr=inputStr.split(' ')
    maxNumber=-1
    for temNum in splitedStr:
        if temNum.isnumeric() and (not temNum.find('9')>=0):
            if int( temNum)>maxNumber:
                maxNumber=int( temNum)
    return maxNumber

           # regexPattern='\d+'
        # batRegex = re.compile(regexPattern)
        # mo3 = batRegex.findall(S)
        # loopFalg=True
        # #if mo3.__len__() >0 :
        # while mo3.__len__() >0:
        #     intList = list(map(int, mo3))
        #     npArrary=np.array(intList)
        #     if str(npArrary.max()).find('9')>=0:
        #         mo3.remove(str(npArrary.max()))
        #     else:
        #         return npArrary.max()
        # return -1

print(ExtractNumber('Another input 9007'))
