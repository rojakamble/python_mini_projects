print("#################################################")
print("###### WELCOME TO ROCK PAPER SCISSORS GAME ######")
print("#################################################")

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]


while True:
    user_input = input("Type Rock/Paper/scissor or Q to quit: ").lower()
    if user_input == "q":
        break
        
    # multiple strings in one line
    # if user_input in ["rock", "paper", "scissors"]: this or below line both are same
    if user_input not in options:
        continue #going back to top of the loop
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    
    computers_pick = options[random_number]
    print("Computer picked", computers_pick + ".")
    
    if user_input == "rock" and computers_pick == "scissor":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and computers_pick == "rock":
        print("You won!")
        user_wins += 1
       
    elif user_input == "scissor" and computers_pick == "paper":
        print("You won!")
        user_wins += 1
    
    else:
        print("You lost!")
        computer_wins += 1
    
 
print("You won", user_wins, "times.")
print("The Computer won", computer_wins, "times.")  
print("Goodbye!")
    