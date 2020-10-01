
8.

x=input("enter string")
letters=0
digit=0
for i in x:
    if i.isalpha():
        letters+=1
    elif i.isnumeric():
        digit+=1
print(letters)        
print(digit)

    