print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to A3JAGBE Treasure Island.\n")
print("Your mission is to find the treasure.") 

start = input("Are you are ready? Y or N\n")

if start == "Y":
  print("Alright let the hunt begin!!!\n")
  print("***********************************************\n")
  
  direction = input("What direction will you like to begin? Left or Right\n")

  if direction == "Left":
    print("Nice Choice ✔️\n")

    activity = input("What will you do? Swim or Wait\n")
    
    if activity == "Wait":
      print("Wise Choice ✔️\n")

      door = input("Which door will you enter? Red, Yellow or Blue\n")

      if door == "Yellow":
        print("****************  🎊 YOU WIN 🎊 ****************\n")
      else:
        print("****************  GAME OVER ****************\n")

    else:
      print("****************  GAME OVER ****************\n")

  else:
    print("****************  GAME OVER ****************\n")

else:
  print("You are welcome back anytime")