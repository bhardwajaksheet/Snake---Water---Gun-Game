import random

computer= random.choice([-1,0,1])       # we used random module to generate random choices for computer 
youstr= input("enter your choice: ")    # we are taking input from the user of his choice 
youDict={ "w": -1 , "s": 1 , "g": 0 }   # we are using dictionary to assign choice to mathametical value
you = youDict[youstr]                   # we are storing the mathametical value 
reverse={1:"snake",-1:"water",0:"gun"}  # just to print the choice
print(f"your choice is {reverse[you]} \n computer choice is {reverse[computer]}")

# games main logic

if (computer == you):
    print("its a draw!")
else:
    if (computer == -1 and you == 0):
        print("you win!")
    elif(computer == -1 and you == 1):
        print("you lose!")
    elif(computer == 1 and you == -1):
        print("you lose!")
    elif(computer == 1 and you == 0):
        print("you win!")
    elif(computer == 0 and you == 1):
        print("you win!")
    elif(computer == 0 and you == -1):
        print("you lose!")
    
