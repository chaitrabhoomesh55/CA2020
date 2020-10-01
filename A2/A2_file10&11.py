import random
y = random.randint(1,10)
print("Lucky number is", y)
x = int(input("guess the lucky number: "))
print("your guess:", x)
count=1
while (count <= 5):
    x = int(input("guess the lucky number: "))
    if (y != x):
        print("Try Again")
        count += 1
    else:
        print("Good Guess")
        break
print("Game over")  
print("Sorry but that was not very Successful")