import random
num = random.randint(1, 10)
print ("Guess the no.between 1 and 10")
guess = int(input("enter your guess:"))
if guess == num:
    print("correct")
else:
    print("wrong! number was:",num)
