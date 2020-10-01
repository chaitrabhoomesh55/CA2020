# x = print( list (range(1,10) ) )
# print( x) 

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print( sum(x) )
res=1
for i in x :
    res = res * i
    print(res)
print("multiplication of all items: ", res)

