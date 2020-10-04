# Write a program to find out the occurrence of a specific word from an alphanumeric statement. 
# Example: 12abcbacbaba344ab  
# Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

s= "12abcbacbaba344ab"
count_a = 0
count_b = 0
count_c = 0
for i in s: 
    if i == 'a': 
        count_a = count_a + 1
    if i == 'b': 
        count_b = count_b + 1
    if i == 'c': 
        count_c = count_c + 1    
print("count of a:", count_a)
print("count of b:", count_b)
print("count of c:", count_c)