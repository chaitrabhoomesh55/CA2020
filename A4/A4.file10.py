10. Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included)

x= [i for i in range(1,21)]
print(x)

res = filter(lambda i: (i%2==0), x)
print(list(res))
