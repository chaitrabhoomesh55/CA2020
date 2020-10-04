14. Create a list of thousand number using range and xrange and see the difference between each other.

a = list(range(1, 1000))
x = list(xrange(1, 1000))
print("the return type of range is:", type(a))
print("the return type of range is:", type(x))

output:
the return type of range is: <class 'list'>
the return type of xrange is: <class 'xrange'>
