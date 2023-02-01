import random

top_num = input("Type a number: ")

# input given will be in the form of string so the below check is done
if top_num.isdigit():
    top_num =int(top_num)
    
    if top_num <= 0:
        print("Please enter a number larger than 0 next time!")
        quit()
else:
    print("Please enter a number only!")
    quit()
    
random_num = random.randint(0, top_num)

# while user_guess != random_num: this also works, here we are trying break keyword
guesses = 0
while True:
    guesses += 1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time!")
        continue #bring us back to top of the loop

    if user_guess == random_num:
        print("You got it!")
        break
    elif user_guess > random_num:
        print("You were above the number!")
    else:
        print("You were below the number!")
    
print("You got it in", guesses, "guesses") 