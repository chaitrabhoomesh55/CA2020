
11. Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
# Hints: Use map() to generate a list.
#      	     Use filter() to filter elements of a list
#             Use lambda to define anonymous functions 


x=[]
x = [i for i in range(1,11)]

square_even = list(map(lambda i: i**2, (filter(lambda i: i%2==0, x ))))
print(square_even)

