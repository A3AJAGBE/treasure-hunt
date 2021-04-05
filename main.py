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
        print("Nice Choice ✅ \n")
        return True
    elif first_response == 'l' or first_response == 'r':
        print("Ouch, not a good start.\n")
        print("****************  ❌ GAME OVER ❌ ****************\n")
        return False
    else:
        print("Invalid Response.\n")
        hunt_func()


def second(second_response):
    if second_response == 'g':
        print("Right Choice ✅ \n")
        return True
    elif second_response == 'p' or second_response == 'b':
        print("That gotta hurt. Try again\n")
        print("****************  ❌ GAME OVER ❌ ****************\n")
        return False
    else:
        print("Invalid Response.\n")
        hunt_func()


def third(third_response):
    if third_response == 'r':
        print("Good Choice ✅ \n")
        return True
    elif third_response == 'l':
        print("Better luck next time 🤞🏽.\n")
        print("****************  ❌ GAME OVER ❌ ****************\n")
        return False
    else:
        print("Invalid Response.\n")
        hunt_func()


def fourth(fourth_response):
    if fourth_response == 'b':
        print("Awesome Choice ✅ \n")
        return True
    elif fourth_response == 'r':
        print("Damn, you were so close, well-done 👏🏽\n")
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

        if first(step_one):
            print("You are at the end of the hallway with three box present.\n"
                  "There is a pink, blue, and green box.")
            step_two = input("(P, B, G): Which will you open? ").lower()

            if second(step_two):
                print("You found a key in the box, with an arrow drawn on plain paper.\n"
                      "There are two directions to proceed (left or right).")
                step_three = input("(L or R): What way to go? ").lower()

                if third(step_three):
                    print("They are two doors, a red and a black door, which you will open with the key found.")
                    step_four = input("(R or B): What is your choice? ").lower()

                    if fourth(step_four):
                        print(f"Congratulations 👏🏽👏🏽👏🏽. Your hunt for {gift} was successful.")
                        print("*************************  YOU WON 🎉️🎉️️ ************************* \n")

    elif start == "No":
        print("Whenever you are ready.")
    else:
        print("Invalid Response.\n")
        hunt_func()


hunt_func()

