

import random
y= random.randint(1,10)
while answer == "Yes" :
    number = int(input("Guess a value: "))
    print("lucky number was:", y)
    if (number == y): 
        print("you guessed lucky number", number)
    elif (number != y):
        answer = str(input("OOps! do you want try again? Yes/No: "))
        print(answer)
        if (answer == "No"):
            break
        else: 
            continue
print("bye")
