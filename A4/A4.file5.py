
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