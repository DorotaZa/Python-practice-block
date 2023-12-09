import random
rock = ("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
paper = ("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
scissors = ("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
game_img = [rock, paper, scissors]

#user choice
user_choice = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER and 2 for Scissors.\n"))
if user_choice >=3 or user_choice < 0:
    print("Ooops! You typed an invalid number.")
else:
    print((game_img[user_choice]))

#indentation of the rest of the code hiper important here! otherwise, will be executed even tho the forst condition wasn't fullfilled
    #random computer choice
    computer_choice = random.randint(0,2)
    print("Computer chose: ")
    print(game_img[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")