# 17. Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.

y = []
x = "catenationtraining"
# x[::-1]
print("reversed string is:", x[::-1] )
for i in x :
    if i in "aeiou":
        y.append(i)
        # y = (",".join(i))
        # print(y)
print("vowel alphabet existing in string:", y ) 
