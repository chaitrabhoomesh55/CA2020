9. # Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}

d={}
for i in range(1,6):
    i = { i : (i*i) } 
    # d = print("".join(i))
    # print(i)
    d.update(i)
    # print(i)
print(d)
