import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:

    user_choose = input("make choose (rock, paper, scissors) to end write (q):  ").lower().strip()

    if user_choose == "q":
        break
    elif user_choose not in options:
        continue
    else:
        computer_choose = options[random.randint(0,2)]
        
        if user_choose == computer_choose:
            print(f"you choose {user_choose} computer choose {computer_choose}")
            print("draw")
            print(f"you {user_wins} : {computer_wins} computer")
            continue
        elif user_choose == "rock" and computer_choose == "scissors":
            print(f"you choose {user_choose} computer choose {computer_choose}")
            print("you win")
            user_wins += 1
            print(f"you {user_wins} : {computer_wins} computer")
            continue
        elif user_choose == "paper" and computer_choose == "rock":
            print(f"you choose {user_choose} computer choose {computer_choose}")
            print("you win")
            user_wins += 1
            print(f"you {user_wins} : {computer_wins} computer")
            continue
        elif user_choose == "scissors" and computer_choose == "paper":
            print(f"you choose {user_choose} computer choose {computer_choose}")
            print("you win")
            user_wins += 1
            print(f"you {user_wins} : {computer_wins} computer")
            continue
        else:
            print(f"you choose {user_choose} computer choose {computer_choose}")
            print("you lost")
            computer_wins += 1
            print(f"you {user_wins} : {computer_wins} computer")
            continue

print(f"final score is you {user_wins} : {computer_wins} computer")
print("good bye")