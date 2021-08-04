def multiplyStrings(s1,s2):
        # code here
        # return the product string
        temp1 = s1
        temp1 = temp1.replace("-","")
        temp2 = s2
        temp2 = temp2.replace("-","")
        if temp1.isnumeric() and temp2.isnumeric():
            return int(s1)*int(s2)
        else:
            return 0

print(multiplyStrings("-120","2"))