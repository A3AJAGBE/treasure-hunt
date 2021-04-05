"""
This application is a basic treasure hunt game.
"""
import random
from logo import logo

print(logo)
print('🚨: Every invalid response, restarts the game.\n')
TREASURES = ['an Airforce 1', 'a MacBook Pro', 'an Xbox']


def first(first_response):
    if first_response == 's':
        print("Continue\n")
        return True
    elif first_response == 'l' or first_response == 'r':
        print("Ouch, Better luck next time \n")
        print("****************  ❌ GAME OVER ❌ ****************\n")
        return False
    else:
        print("Invalid Response.\n")
        hunt_func()


def hunt_func():

    start = input("(Yes or No): Are you are ready to begin? ").title()

    # Verify the question response
    if start == "Yes":
        gift = random.choice(TREASURES)
        print(f"The hunt is for {gift}.\nBe Careful and Happy hunting.")
        print("***********************************************\n")

        print("You are currently at the starting point.\nThere are three directions in front of you"
              " (straight, left or right).")
        step_one = input("(S, L OR R): How do you want to proceed? ").lower()

        first(step_one)


    elif start == "No":
        print("Whenever you are ready.")
    else:
        print("Invalid Response.\n")
        hunt_func()


hunt_func()

