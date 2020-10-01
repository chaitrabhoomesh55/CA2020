
# 8. Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}      **Expected Result: {1:10,2:20,3:30,4:40}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40} 


a={1:10,2:20}
b={3:30,4:40}
c = {}
for d in (a, b): 
    c.update(d)
    print(c)
