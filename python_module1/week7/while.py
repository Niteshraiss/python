# x = int(input("Enter number"))
# t = input('Enter')
# while x:
#     if t == '#':
#         print("continue\n")
#         continue
#     if t == 'done':
#         print('ending')
#         break
# print("Done while")

while True:
    x = input('>')
    if x[0] == '#':
        continue
    if x == 'done':
        print('Getting out')
        break
    print('Continuing')
