# 16. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number 
# which is divisible by 3 and a multiple of 2.

y = []
x = list( range(1, 100) )
for i in x:
    if (i % 3 == 0) and (i % 2 == 0):
        y.append(str(i))
print(y)
