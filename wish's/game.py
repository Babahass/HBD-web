import random
import os

def games():
     print("welcome to rock ,paper, scissors")

     choices=["rock","paper","scissor"]
     player_choice= input("enter your choice (rock, paper,scissor): ").lower()

     if player_choice not in choices:
         print("invalid choice . please try again,")
         return
     computer_choice = random.choice(choices)
     print(f"the computer chose {computer_choice}")

     if player_choice == computer_choice:
         print("its a tie")
     elif   (player_choice=="rock" and computer_choice=="scissor")or \
            (player_choice=="paper" and computer_choice=="rock")or \
            (player_choice=="scissor" and computer_choice =="paper"):
         print("you win")
     else:
         os.remove("C:\Users\Mohammed\Documents\rock paper scissor")

         games()