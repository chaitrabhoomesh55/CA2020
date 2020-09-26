
# 8.
l1=[]
l2 =[]
x=input("enter string")
letters=0
digit=0
for i in x:
    if i.isalpha():
        letters+=1
        l1.append(letters)
        print(l1)
        # i+=1
    elif i.isnumeric():
        digit+=1
        l2.append(digit)
    print(l2)
    # else: 
    #     i+=1
    # else:
    #     
    # print