# 7.1.Write a program that calculates and prints the value according to the given formula: 
# Q = Square root of [(2*C*D)/H] 
# Following are the fixed values of C and H: 
# C is 50. H is 30. 
# D is the variable whose values should be input to your program in a comma-separated sequence. 

 
input1 = input("enter value: ")    # input:200,250,100   
D = (input1.split(","))             # 0utput:[26, 29, 18]
C=50
H=30
list2=[]
  
for i in D:
    phras = ((2*C*int(i))/H)**(1/2)
    print(phras)
    list2.append(round(phras))
    # list2 = print(",".join(round(phras)))
print(list2)



2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default. 

class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        self.l = l
        self.Shape = 0        
    def area(self, l):
        area = l * l
        print("area of square is:", area)
        return area

A1 = Square(20).area(20)

3. Create a class to find the three elements that sum to zero from a set of n real numbers. 
Input array: [-25,-10,-7,-3,2,4,8,10] 
Output: [[-10,2,8],[-7,-3,10]] 

class sumzero():
    def functn(arr, n):   
        pair1 = [] 
        pair2 = []
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (arr[i] + arr[j] + arr[k] == 0):
                        pair1 = print([arr[i], arr[j], arr[k]])
                # pair2.append([pair1])

arr = [-25,-10,-7,-3,2,4,8,10]
n = len(arr)
inst = sumzero()
inst2= inst.functn(arr, n)

4. What is the output of the following code? Explain your answer as well. 

class Test: 
	def __init__(self): 
        self.x = 0 
class Derived_Test(Test): 
	def __init__(self): 
        self.y = 1 
def main(): 
	b = Derived_Test() 
	print(b.x,b.y) 
main() 
  
Output:- 
TabError: inconsistent use of tabs and spaces in indentation
AttributeError: 'Derived_Test' object has no attribute 'x'
Reason- class Derived_Test doesn not have variable x defined in it. 
To use the oject of Class test the Derived_Test class should have Test.__init__(self).


class A: 
	def __init__(self, x= 1): 
        self.x = x 
class der(A): 
	def __init__(self,y = 2): 
    	super().__init__() 
        self.y = y 
def main(): 
	obj = der() 
	print(obj.x, obj.y) 
main()) 

SyntaxError: unmatched ')'
Reason- extra paranthese at the calling of main function

class A: 
	def __init__(self,x): 
        self.x = x 
	def count(self,x): 
        self.x = self.x+1 
class B(A): 
	def __init__(self, y=0): 
    	A.__init__(self, 3) 
        self.y = y 
	def count(self): 
        self.y += 1      
def main(): 
	obj = B() 
    obj.count() 
	print(obj.x, obj.y) 
main() 

Output: PS C:\Users\ADMIN\chai> & C:/Users/ADMIN/anaconda3/python.exe c:/Users/ADMIN/chai/python_codes/OOPS.py
  File "c:/Users/ADMIN/chai/python_codes/OOPS.py", line 3
    self.x = x 
              ^
TabError: inconsistent use of tabs and spaces in indentation
 thats because of inter-platform tab inconsistencies, specially when you change either an editor and/or OS.
 NameError: name 'B' is not defined
thats because The class objects are defined at the class level not inside a method.

●	class A: 
	def __init__(self): 
        self.multiply(15) 
    	print(self.i) 
  
	def multiply(self, i): 
        self.i = 4 * i; 
class B(A): 
	def __init__(self): 
    	super().__init__() 
  
	def multiply(self, i): 
        self.i = 2 * i; 
obj = B() 

Output : 30

5. # Create a Time class and initialize it with hours and minutes. 
# Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min) 
# Make a method displayTime which should print the time. 
  
# Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute. 

class Time():
	def __init__(self, h, m):
		self.h = h
		self.m = m
	def addTime(t1, t2):
		T = Time(0, 0)
		T.h = t1.h + t2.h
		T.m = t1.m + t2.m
		if (t1.m + t2.m) > 60:
			T.h += 1
			T.m -= 60
		return T
		print("{T.h} hr and {T.m} min".format(T.h, T.m))
		# return 
	def displayTime(self):
		print("Time is %d hr and %d min" %(self.h, self.m))
	def DisplayMinute(self):
		totalminutes = print((self.h*60) + (self.m), "minutes") 
		return totalminutes

k = Time(2, 50)
l = Time(1, 20)
# a = Time()
t3 = Time.addTime(k,l)
t3.displayTime()
t3.DisplayMinute()
	
6. # .  Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, 
# as a parameter. The constructor must assign initialAge to age after confirming the argument passed as initialAge is not
#  negative; if a negative argument is passed as initialAge , the constructor should set age to 0  
#  and print Age is not valid, setting age to 0. In addition, you must write the following instance methods:

# yearPasses()should increase the  instance variable by .
# amIOld()should perform the following conditional actions:
# If  age<13, print You are young..
# If  age >=13 and age<18, print You are a teenager.
# Otherwise, print You are old.

class person():
    def __init__(self, initialage):
        self.age = initialage
        if initialage < 0:
            print("Age is not Valid, setting age to 0")
            self.age = 0
        else:
            self.age = initialage
    def yearPasses(self):
        self.age += 1

    def amIOld(self):
        if (self.age>=1 and self.age<13):
            print('You are young.')
        elif (self.age>=13) and (self.age<18):
            print('You are a teenager.')
        elif (self.age>18):
            print('You are old.')
        else:
            print('Age is not Valid, setting age to 0')

x = person(14)
y = x.amIOld()







