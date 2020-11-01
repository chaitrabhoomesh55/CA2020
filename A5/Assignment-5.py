
1. Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError

example1:

try:
    items = [1,2,3,];
    # value=[]
    for d in items:
    # value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
        value.append(int(2*d));
        print (''.join(value))
except(TypeError, SyntaxError, NameError):
    print("Error Occured and Handled")
else:
    print('no error occured')

example2:

try:
    sum = 1+Consultadd;
    print ('sum')
except (SyntaxError, NameError):
    print("Syntax Error")

2. Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect throw an 
exception and ask them to enter the name again. Make sure to use read only mode.

import sys

src=sys.argv[1]
# with open(src, 'r') as fin (myfile.txt, 'r')
myfile = open(myfile.txt, 'r')
try:
    if myfile == myfile.txt:
        pass
except(NameError, ValueError):
    print("Error Occured opening file")
    myfile = input("Enter file name again:")

content = myfile.readlines()
print(content)

3. Write a program to handle an error if the user entered the number more than four digits it should return “Please length 
is too short/long !!! Please provide only four digits” 


try:
    user = (input("enter a number:"))
    astring= str(user)
    length=len(astring)
    if (length == 4):
        print(user);
    else:
        print('length entered is too short/long! Please provide only four digits')
except(SyntaxError, ValueError, NameError, TypeError):
    print('error occured and handled')




4. Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and 
if the password is incorrect give chance to enter it again but it should not be more than 3 times.


for i in range(3):
    # try:
    #     username = Chai
    #     password = 'Pass123'
        username = input("Enter user name: ")
        password= (input("Enter password: ")
        re_enter_password= eval(input("Please re-enter the password: "))
        if password!=re_enter_password:
            raise ValueError
        else:
            print("Account is successfully created")
            break
    except:
        print("Incorrect password. Please try again")


5. https://www.programiz.com/python-programming/exception-handling Go through this link to understand Finally and Raise concept.

6. Read any file using Python File handling concept and return only the even length string from the doc.txt file.
    Consider the content as: 
	Hello I am a file 
	Where you need to return the data string 
	Which is of even length 
	Make sure you return the content in 
	The same link as it is present.


x=open('file1.txt','r')
data=x.readlines()
for i in data:
    word=i.split(' ')
    for j in words:
        if(len(j%2==0)):
            print (j)