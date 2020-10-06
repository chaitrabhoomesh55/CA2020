1. Write a program to reverse a string.
Sample data: “1234abcd”
Expected Output: “dcba4321”

def reverse(x):
    x = x[::-1]
    print(x)

x ="1234abcd"
reverse(x)

2.
Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
Expected Output:
No. of Upper case characters : 3
No. of Lower case Characters : 12


def count_case(s):
    lower=0
    Upper=0
    for i in s:
        if ( i.islower() ):
            lower += 1
        else:
            Upper += 1
    print("No. of lower case characters:", lower)
    print("No. of Upper case characters:", Upper)


s = input("enter the string:")
count_case(s)

3. # Create a function that takes a list and returns a new list with unique elements of the first list.

def unique_list(list):
    unique =[]
    for i in list:
        if i not in unique:
            unique.append(i)
    print(unique)

list = [1, 2, 3, 4, 6, 7, 3, 4, 6, 2]
unique_list(list)  
        
4. Write a program that accepts a hyphen-separated sequence of words 
# as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.


def sort_list(h):
    items= [n for n in h.split('-')]
    items.sort()
    print('-'.join(items))

h = input("enter hyphen seaparated values:")
sort_list(h)


5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

def capitalize_list(lines):
    lines = []
    while True:
        l = input()
        if l:
            lines.append(l.upper())
        else:
            break
    for i in lines:
        print(i)

# print(input("enter the sequence of lines:\n"))
lines=[]
capitalize_list(lines)       

6. Define a function that can receive two integral numbers in string form and compute their sum and print it in console.


def calculate_sum(a,b) :
    s = int(a) + int(b)
    print(s)


x = input("enter num1: ")
y = input("enter num2: ")

calculate_sum(x, y)

7. Define a function that can accept two strings as input and print the string with maximum length in console. 
# If two strings have the same length, then the function should print all strings line by line.

def compare_str(x, y):
    if (len(x) > len(y)):
        print(x)
    elif (len(y) > len(x)):
        print(y)
    else:
        print(x)
        print(y)

x = input("enter string1: ")
y = input("enter string2: ")
compare_str(x, y)

8. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

def square_num(l):
    for i in range(1, 20):
        i = i**2
        l.append(i)
    print(tuple(l))

l=[]
square_num(l)


 9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit 
# with a label to identify the even and odd numbers. 
# Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def show_Numbers(limit):
    for i in range(0, limit):
        if i % 2 == 0 :
            print(i, "EVEN")
        elif i % 2 != 0:
            print(i, "ODD")

limit =int(input("Limit is:"))
show_Numbers(limit)            


10. Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included)

x= [i for i in range(1,21)]
print(x)

res = filter(lambda i: (i%2==0), x)
print(list(res))

11. Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
# Hints: Use map() to generate a list.
#      	     Use filter() to filter elements of a list
#             Use lambda to define anonymous functions 


x=[]
x = [i for i in range(1,11)]

square_even = list(map(lambda i: i**2, (filter(lambda i: i%2==0, x ))))
print(square_even)





12. Write a function to compute 5/0 and use try/except to catch the exceptions 

def error():
    return 5/0


try: 
    error()
except ZeroDivisionError:  
    print("division by zero")
except Exception.err:
    print("encountered an exception")
finally:
    print("try again & input non-zero values")



13.  # 13. Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 


# From functools import *
import functools

x= [[1,2,3],[4,5],[6,7,8]]

endstring = functools.reduce(lambda a, b: a+b, x)
print(endstring)

delimeter = ''
finalstr = functools.reduce(lambda a, b: str(a) + delimeter + str(b), endstring)
print(finalstr)


14. What is the output of the following codes:


def foo():
    try:
       return 1
    finally:
        return 2

k = foo()
print(k)


# Output: 2


def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')

a()

# output:
# after f
# Traceback (most recent call last):
#   File "c:/Users/ADMIN/chai/python_codes/TP.py", line 24, in <module>
#     a()
#   File "c:/Users/ADMIN/chai/python_codes/TP.py", line 17, in a
#     f(x, 4)
# TypeError: 'int' object is not callable