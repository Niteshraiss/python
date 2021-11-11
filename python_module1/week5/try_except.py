me = "Nitesh"
try:
    no = int(me)
except:
    no = 10
print("First ", no)

me = '1'
try:
    no = int(me)
except:
    no = -1
print("Second", no)
