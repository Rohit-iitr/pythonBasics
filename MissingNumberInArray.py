def MissingNumber(array,n):
        # code here
        toReturn = 0
        sumOfArray=sum(array)
        sumOfNum=int(n*(n+1)/2)
        print(sumOfNum-sumOfArray)

        # if n>2:
        #     for num in range(1,n):
        #         if not num in array:
        #             toReturn=num
        #             break
        #         else:
        #             toReturn=n

        # else:
        #     if not array[0]==1:
        #         toReturn=1
        #     else:
        #         toReturn=2
        

print(MissingNumber([1],2))