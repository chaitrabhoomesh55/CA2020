# Write a program in Python to complete the following task:
# ●	Create two different list as in even_list and odd_list
# ●	Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the even_list 
# and if the entered number is odd append it to the odd list.
# ●	Keep that in mind you can only add 5 items in each list
# # ● Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.

even_list = []
odd_list = []

count_a=0
count_b=0
while (count_a < 5) and (count_b < 5):
    n=int(input("Enter number of elements in range(1, 50):"))
    if n % 2 == 0:
        even_list.append(n)
        count_a += 1
    else:
        odd_list.append(n)
        count_b += 1
print("even number list:", even_list)
print("odd number list:", odd_list)