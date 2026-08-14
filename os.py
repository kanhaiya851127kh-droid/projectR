import random 
import os 

number = random.randint(1, 10)
guess = input("Guess the number between 1 and 10: ")
guess = int(guess)

if guess  == number:
    print("you won !")
else:
  print("you lost ! ")
  print("currect number was :",number)
