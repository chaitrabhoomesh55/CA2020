2. Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
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