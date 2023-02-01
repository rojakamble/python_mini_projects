print("########################################")
print("######### Welcome to Adventure #########")
print("########################################")

print("You are going to find a GOLD coin during your adventure, if you get, you win, or you are lost! ")
print("##### Warnings!! will be notified, you are on your own risk at this adventure ##### ")
print("You will take home the real GOLD coin of 250 grams of worth $15000, if you win !!! ")

name = input("Type your name: ")
print("Welcome to this adventure!", name)

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way you would like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or you can swim across the river, so what you want to do (swim/walk)? ")
    if answer == "swim":
        print("If You swim, there is threat of an alligator.")
    elif answer == "walk":
        print("You walked for many miles, you are low on water, might lose the game!")
    else:
        print("Not a valid option. You are lost.")
    
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back to main road. Then adventure ends!")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        if answer == "yes":
            print("You talk to stranger and they give you GOLD coin. You Win!") 
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You are lost.")  
    
else:
    print("Not a valid option. You are lost.")
    
print("Thank you for trying", name, "!!!")