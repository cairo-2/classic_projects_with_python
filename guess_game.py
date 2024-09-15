import random

user_number = input("enter a number: ")

if user_number.isdigit():
    user_number = int(user_number)

    if user_number <= 0:
        print("enter a number <= 0")
        quit
else:
    print("enter a number not a text")
    quit

random_number = random.randint(0, user_number)

user_try = 0

while True:
    user_try += 1
    user_guess = input("guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("enter a number not a text")
        continue

    if user_guess == random_number:
        print("good")
        print(f"you git it in the {user_try}th time")
        break
    elif user_guess > random_number:
        print("it is lower")
    else:
        print("it is biger")

    
