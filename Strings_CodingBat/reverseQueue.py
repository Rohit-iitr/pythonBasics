def rev(q):
    print(q)
    stack = []
    tempQ = q
    for countr in range(q.__len__()):
        stack.append(tempQ.pop())
    # q = []
    for item in stack:
        q.append(item)
    return q


print(rev([1, 2, 3, 4, 5]))
