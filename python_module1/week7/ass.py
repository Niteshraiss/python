l = None
s = None
while True:
    val = input('Enter number')
    if val == 'done':
        break
    try:
        ival = int(val)
    except:
        print('Invalid input')
        continue
    if l is None or(ival > l):
        l=ival
        print("Greater",l)
    if s is None or(ival < s):
        s=ival  
        print("Smaller",s)  
print("Maximum is", l)
print("Minimum is ", s)
