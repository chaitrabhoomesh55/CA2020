# Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# t = [1,2,3,4,5,6,7,8,9,10]
t=[]
x=[]
for i in range(1, 11):
    t.append(i)
    if i % 2  == 0:
        x.append(i)
print("even number in tuple:", tuple(x))
print(tuple(t))
