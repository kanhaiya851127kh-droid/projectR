import random

secret = random.randint(1, 10)

guess = int(input("1 se 10 ke beech number guess karo: "))

if guess == secret:
    print("Correct Guess 👍")
else:
    print("Wrong ❌ Number tha:", secret)