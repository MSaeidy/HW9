# imports and global variables
import random


User_choices = ['rock' , "paper", "scissor"]


# create a function to get user input
def get_user_input():
    choice =input("pick your choice : [\'rock\' , \"paper\", \"scissor\"]:  ")
    while choice not in User_choices:
        choice =input("pick your choice : [\'rock\' , \"paper\", \"scissor\"]:  ")
    return choice


# crate a function to get pc input
def get_pc_input():
    pc_choice = random.choice(User_choices)
    print(f"pc choice was: {pc_choice}")
    return pc_choice



# compare and detemine with one is winner
def determine_winner(user_input , pc_input):
    if user_input == pc_input:
        return print("DRAW !")
    elif (user_input == "rock" and pc_input == "scissor") \
            or (user_input == "scissor" and pc_input == "paper") \
            or (user_input == "paper" and pc_input == "rock"):
        print("user win !")
    else:
        print("computer win !")


# create a main function as the runner
def main():
    user_input =get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input,pc_input)
    print("end of program")



# make an iteration for doing the game as much as we need
answer = "y"
while answer == "y":
    main()
    answer = input("do you want to continue? (y/n): ")
