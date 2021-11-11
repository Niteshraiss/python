no = input("Enter number")
try:
    first = int(no)
    first = first+10
except:
    print("You need to provide number and not", no)
print(first)
