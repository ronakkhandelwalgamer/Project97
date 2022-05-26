
import random
print ("Number guessing game")
number = random.randint(1,9)
chances=0
print("Guess a number (between 1 and 9)")

while chances < 5:

    guess = int(input("Enter Your Guess:-"))
 
    
    if guess == number:
        print("Congratulation You Won!!!")
            # break
    
    elif guess < number:
         print("Your guees was to lower : Guess a number higher than ", guess  ) 

    else:
        print("Your guees was to higher : Guess a number lower than ", guess )

        chances+=1

    if not chances < 5:
         print("You LOSE!!! The number is",number )   

