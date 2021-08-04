# def replaceFun(str):
#     strLength = len(str)
#     if strLength == 0 or strLength == 1:
#         return str
#     smallStr = replaceFun(str[1:])
#     if str[0]+smallStr[0] == 'pi':
#         return '3.14'+smallStr[1:]
#     else:
#         return str[0]+smallStr
def replaceFun(str):
    strLength = len(str)
    if strLength == 0 or strLength == 1:
        return str
    smallStr = replaceFun(str[1:])
    if str[0] == smallStr[0]:
        return str[0]+smallStr[1:]
    else:
        return str[0]+smallStr


print(replaceFun('xxxxff'))
