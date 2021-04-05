"""
This application is a basic treasure hunt game.
"""
import random
from logo import logo

print(logo)
print('🚨: Every invalid response, restarts the game.\n')
TREASURES = ['an Airforce 1', 'a MacBook Pro', 'an Xbox']


def hunt_func():

    start = input("(Yes or No): Are you are ready to begin? ").title()

    # Verify the question response
    if start == "Yes":
        gift = random.choice(TREASURES)
        print(f"The hunt is for {gift}.\nBe Careful and Happy hunting.")
        print("***********************************************\n")

    elif start == "No":
        print("Whenever you are ready.")
    else:
        print("Invalid Response.\n")
        hunt_func()


hunt_func()

