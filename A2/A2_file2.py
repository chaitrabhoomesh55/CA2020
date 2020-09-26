print('what you want to do with this')
i=int(input('for addition press 1 and for sub press 2 for multi press 3 for div press 4'))
print('plese enter two no')
a=int(input('enter first no'))
b=int(input('enter second no'))

def add(a,b):
    print(' sum of two no',a+b)
def sub(a,b):
    print('sub of two no',a-b)
def mul(a,b):
    print('mul fo two no',a*b)
def div(a,b):
    print('div of two no',a/b)

if i==1:
    add(a,b)

if i==2:
    sub(a,b)

if i==3:
    mul(a,b)

if i==4:
    div(a,b)
else:
    print("negative")    