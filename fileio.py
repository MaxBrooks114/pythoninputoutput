# jabber = open("/Users/maxbrooks/original.txt",'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#          print(line, end = '')
#
# jabber.close()

# with open("/Users/maxbrooks/original.txt",'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end = '')
# with open("/Users/maxbrooks/original.txt",'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')

# with open("/Users/maxbrooks/original.txt",'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

#
# with open("/Users/maxbrooks/original.txt",'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')


with open("/Users/maxbrooks/original.txt",'r') as jabber:
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end='')



