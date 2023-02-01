print("######## WELCOME ########")
print("######## GAME TIME ########")

playing = input("Do you want to play quiz? ")
if playing.lower() != 'yes':
    quit()
else:
    print("Okay, lets play!")
    
score = 0
print("###### You are going to tell some acrynoms for the given abbrevations ######")
    
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does NASA stand for? ")
if answer.lower() == "national aeronautics and space administration":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does NEWS stand for? ")
if answer.lower() == "north east west south":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PC stand for? ")
if answer.lower() == "personal computer":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You have scored " + str(score) + " points!")
