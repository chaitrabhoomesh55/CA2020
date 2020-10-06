8.Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

def square_num(l):
    for i in range(1, 20):
        i = i**2
        l.append(i)
    print(tuple(l))

l=[]
square_num(l)
