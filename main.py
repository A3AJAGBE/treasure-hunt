"""
This application is a basic treasure hunt game.
"""

from logo import logo

# Displays at the beginning
print(logo)
print("Welcome on this awesome adventure\n")

start = input("Are you are ready to begin? Yes or No \n").title()

# Verify the question response
if start == "Yes":
    print("Alright let the hunt begin!!!\n")
    print("***********************************************\n")

    direction = input("What direction will you like to begin? Left or Right\n").title()

    if direction == "Left":
        print("Nice Choice ✅ \n")
    elif direction == "Right":
        print("****************  ❌ GAME OVER ❌ ****************\n")
    else:
        print("Invalid Response")

elif start == "No":
    print("Restart the game, when you are ready")
else:
    print("Invalid Response")
