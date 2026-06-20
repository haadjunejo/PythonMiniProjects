# Random Number Guessing Game
import random
target = random.randint(1,100)

userguess = ()
while userguess!=target:

    userguess = input("Enter your guess or Quit(Q) : ")

    if(userguess.upper()=="Q"):
        print("you decided to quit!")
        break

    guessNumber = int(userguess)   

    if(guessNumber==target):
        print("congratulation you guess correct!")        
        print("Actual Number was : ",target)
        break
    elif(guessNumber>target):
        print("your guess is greater than actual number")
    elif(guessNumber<target):    
        print("your guess is lesser than actual number")
    

print("-------GAMEOVER--------")

                