# 7. Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]
a=[1, 3, 5, 7, 9, 10] 
b = [2, 4, 6, 8]
a.extend(b)
a.pop(5)
print (a)
