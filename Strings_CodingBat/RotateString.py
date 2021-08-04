#User function Template for python3



#Function to check if a string can be obtained by rotating
#another string by exactly 2 places.
def isRotated(str1,str2):
    flagAntiCloclwise = False
    flagCloclwise = False

    if (len(str1)>1 and len(str2)>1):
        count =0
        index =2
        y=''
        while count< len(str1):
            if  index+count<len(str1):
                y=y+str1[index+count]
            else:
                y=y+str1[index+count-len(str1)]
            count+=1
            #index+=1
       
        
        if y==str2:
            flagCloclwise=True
            
        count =0
        index =-2
        y=''
        while count< len(str1):
            if  index+count<len(str1):
                y=y+str1[index+count]
            else:
                y=y+str1[index+count-len(str1)]
            count+=1
            #index+=1
        
        if y==str2:
            flagAntiCloclwise=True
            
    return int(flagAntiCloclwise or flagCloclwise)

        

print(isRotated('AB','AB'))