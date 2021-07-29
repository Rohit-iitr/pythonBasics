def is_valid(s):
		# Code here
        inputStr = s
        if inputStr.__len__()==12 and inputStr[:2]=='91':
            if inputStr[2]=='7' or inputStr[2]=='8' or  inputStr[2]=='9':
                return 1
            else:
                return 0 
        elif inputStr.__len__()==11 and inputStr[0]=='0':
                    if inputStr[1]=='7' or inputStr[1]=='8' or  inputStr[1]=='9':
                        return 1
                    else:
                        return 0
        if inputStr.__len__()==10 and (inputStr[0]=='7' or inputStr[0]=='8' or  inputStr[0]=='9'):
                        return 1
        else:
            return 0

print(is_valid('915164627691'))