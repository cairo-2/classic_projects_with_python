print("wellcome........")

playing = input("start (y) (n) ").lower().strip()    # start option 
if playing != "y":
    quit()
    
print("let's go ......")
score = 0

anser = input("what is the capital of egypt? ").lower().strip()    # first question
if anser == "cairo":
    print("correct")
    score += 1
else:
    print("wrong")

anser = input("what is the capital of nigeria? ").lower().strip()    # third question
if anser == "abuja":
    print("correct")
    score += 1
else:
    print("wrong")

anser = input("what is the capital of usa? ").lower().strip()    # secsecond question
if anser == "washington":
    print("correct")
    score += 1
else:
    print("wrong")

print(f"the end of the game \n your score is {score} \n it is {(score / 3)*100:.02f} %")