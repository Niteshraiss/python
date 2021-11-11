small = None
for i in [10, 1, 1, 0, 4, 5, 2, 9]:
    if small is None:
        small = i
        print('value of small', small)
    elif i < small:
        print('value of i', i)
        small = i
    print(small, '\t', i)
print('Smallest', small)
