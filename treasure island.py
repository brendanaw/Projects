print('''
*******************************************************************************
   ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88   
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_move = input("You reached a fork in the road, pick left or right.\n").lower()

if first_move== "left":
  second_move = input('You\'ve reached a river and need to get across. Type "swim" to go ahead or "wait" for a boat to arrive.\n').lower()
  if second_move == "wait":
    third_move = input('You\'ve encounter 3 doors. Pick "Red", "Blue" or "Yellow".\n').lower()
    if third_move == "yellow":
      print("Congrats, you\'ve won!'")
    elif third_move == "red":
      print("You got burned by fire, game over!'")
    elif third_move == "blue":
      print("You got eaten by wild beasts, game over!'")
    else:
      print("Game over!'")
  else:
    print("You\'re dead! A wild Magikarp appeared and bit you. Try again.")
else:
  print("You\'re dead! Try again.")

