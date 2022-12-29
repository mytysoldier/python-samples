# with open('files/test.txt') as f:
#     # s = f.read()
#     # print(s)
#     for _ in range(4):
#         s_line = f.readline()
#         print(s_line)
#         if s_line == '':
#             print('fin')

with open('files/test.txt') as f:
    s_line = f.readlines()
    print(s_line)