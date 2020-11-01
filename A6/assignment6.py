1. Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.

x = list(filter(lambda x: x%3!=0 and x%7==0,x))  
print(x)


2. Write a program in Python to  multiple the element of list by itself using a traditional function and 
pass the function to map to complete the operation. 


my_list = [1, 2, 3, 4, 5, 6]
l = (map(lambda x: x*x, my_list))
print(list(l))


3. Write a program to Python find out the character in a string which is uppercase using list comprehension

str1 = "PyThONstRiNg"
str2 = (filter(lambda x: x.isupper(), str1))
print(str2)


4. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects.
# The dictionary should maps students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension.
# HINT-Use Zip function also 


student = ['Smit', 'Jaya', 'Rayyan'] 
capital = ['CSE', 'Networking', 'Operating System'] 
dict1 = dict(zip(student, capital))
print(dict1) 
 
 
5.  Learn More about Yield, next and Generators 

Understanding Generators:

So far, you’ve learned about the two primary ways of creating generators: by using generator functions and generator expressions.
You might even have an intuitive understanding of how generators work. 
Let’s take a moment to make that knowledge a little more explicit.

Generator functions look and act just like regular functions, but with one defining characteristic. 
Generator functions use the Python yield keyword instead of return. Recall the generator function you wrote earlier:

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
This looks like a typical function definition, except for the Python yield statement and the code that follows it. 
yield indicates where a value is sent back to the caller, but unlike return, you don’t exit the function afterward.

Instead, the state of the function is remembered. That way, when next() is called on a generator object 
(either explicitly or implicitly within a for loop), the previously yielded variable num is incremented, and then yielded again.
Since generator functions look like other functions and act very similarly to them, 
you can assume that generator expressions are very similar to other comprehensions available in Python.




6. Write a program in Python using generators to reverse the string. Input String = “Consultadd Training” 

def reverse(x):
    for i in range(len(x)-1,-1, -1):
    yield x[i]
    
x = list(input("enter the string to be reversed: "))
# x = “ConsultaddTraining”
for char in reverse(x):
    print(char, end = "")


7. Write any example on decorators.
Functions that take other functions as arguments are called higher order functions.


def dec(func):
    def inner(a, b):
        print("Mult of {0} and {1} is:".format(a,b))
        if a == 0 or b == 0:
            print("Oops I cannot mult with 0 argument, Try again.")
        return func(a, b)
    return inner

@dec
def mult(a, b):
    mult = a * b
    print(mult)
    return mult

A = mult(9, 7)


8. Learn about What is FRONT END and its Technologies and Tools 
●	Make sure to mention at least 5 top notch technologies of Frontend. 
●	Also mentioned the name of companies using those 5 technologies individually 

Front-end Web Development refers to building web interfaces, specifically the parts of the website that the user will interact 
with. When you’re browsing the web, everything you see, from images and headings to sliders and buttons is made using HTML, CSS 
and JavaScript, the main components to any website.

Back-end Development refers to the parts of the website that a user doesn’t see or directly interact with. 
The back end handles application logic, algorithms, database interaction and the processing of user requests.

In this section, you will learn how to make Python Web applications more user friendly by leveraging the power of both the 
Front-end and Back-end. 
These articles cover how to integrate Back-end frameworks like Flask and Django with popular Front-end libraries and frameworks.

Technologies:
1. Axios - A popular JavaScript library designed to handle HTTP requests in the browser and Node.js ecosystem. 
Axios is often used together with frameworks like React or Vue.js, but can be used just as well with vanilla JavaScript
2. Material-UI - One of the world's most popular React UI libraries used for faster and easier web development.
 in the world for (backed by a community of over 1 million developers in 180+ countries.
3. NgRx - A framework for building reactive applications in Angular. NgRx provides state management, 
isolation of side effects, entity collection management, router bindings, code generation, and developer tools that enhance 
developers experience when building many different types of applications.
4. AppRun - A JavaScript library for developing high-performance and reliable web applications using the elm inspired architecture,
 events, and components.
5. SSR - Stands for server-side rendering. SSR is a popular technique for rendering a normally client-side only single page app 
(SPA) on the server and then sending a fully rendered page to the client. 
6. Angular Universal - The process of server-side rendering (SSR) an application to HTML on the Server (ie: Node.js). 
Typical Angular applications are Single-Page Applications (aka SPA's) where the rendering occurs on the Browser.


1. React for a Responsive Web Front-End Development - Airbnb, Dropbox, BBC, Facebook, New York Times, and Reddit.
2. Angular Front-End Development - Netflix, Upwork, IBM, Goodfilms, Freelancer, Gmail, Paypal, and The Guardian 
3. Vue.js Web App Front-End Development - 9gag, Nintendo, GitLab, Behance, and Laravel. 
4. Ionic for Cross-Platform Front-End Development - The National Health Service, GE Transportation, Market Watch, and Amtrak 
5. Flutter for Cross-Platform Mobile and Web Front-End Development - Google ads, Alibaba, Birch Finance, Cryptograph, and Hookle are some of the applications powered by Flutter.




