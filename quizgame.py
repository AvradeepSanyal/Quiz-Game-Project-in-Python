print("Welcone to my computer quiz!")

playing = input("Do you want to play (y/n)?").lower()
score = 0
if playing == 'y':
    print("Lets Play!")
elif playing == 'n':
    print("Ok see you again!")
    quit()
else:
    print("Invalid Output")

answer = input("What does CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ").lower()
if answer == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stands for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("Your score is ", score)
