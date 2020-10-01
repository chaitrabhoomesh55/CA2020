

6. # Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

def square_list () :
    l = list()
    for i in range(1, 30):
        i = (i**2)
        l.append(i)
    print( l[:5] )
    print( l[-5:] )


square_list ()
