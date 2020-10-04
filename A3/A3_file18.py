
# Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even length of word.
z=[]
y = ("hello my name is abcde")
x = y.split()
count=0
print(x)
for i in x:
    if (len(i) % 2 == 0) and (count < 5):
        z.append(i)
print("strings which has even length of word:", z)   
    