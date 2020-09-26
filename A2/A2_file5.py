list=[]
x = int(input("enter a value between 2000-3200: "))
for i in range(2000,3200):
    if ((i%7) == 0) and ((i*5) != 0):
        list.append(str(i))
print(','.join(list))
        