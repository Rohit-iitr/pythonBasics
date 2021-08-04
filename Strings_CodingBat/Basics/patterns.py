num = 4
row = 0
# while row <= num:
#     col = num
#     while col >= 1:
#         print(col, end='')
#         col -= 1
#     print()
#     row += 1
col = 1
# while row <= num:
#     # col = row
#     for x in range(0, row):
#         print(col, end='')
#         col += 1
#     print()
#     row += 1

while row < num:
    # col = row
    starChr = ord('A')
    for x in range(0, num):
        print(chr(starChr+x), end='')
        col += 1
    print()
    row += 1
