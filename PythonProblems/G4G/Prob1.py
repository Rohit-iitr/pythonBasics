def strstr(s,x):
    occurenece =0
    flag = False
    if len(s)==0 or len(x)==0:
        occurenece =-1
    else:
        while occurenece<=len(s)-len(x):
            print(s[occurenece:occurenece+len(x)])
            if s[occurenece:occurenece+len(x)] == x:
                flag=True
                break
            else:
                occurenece+=1

        if not flag:
            occurenece=-1

    return occurenece




print(strstr('abcabcabcd','abcd'))