def getOddOccurrence(arr, n):
        # code here 
        dic={}
        for num in arr:
            if num in dic.keys():
                dic[num]+=1
            else:
                dic[num]=1
        print(dic)
        for key,Value in dic.items():
            if not Value%2==0:
              break
        return key


print(getOddOccurrence([5,2],7))