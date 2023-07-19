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
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
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
print("\nWelcome to Treasure Island.")
print("Your mission is to find the treasure.")


# noinspection SpellCheckingInspection
def t_island():
    while True:
        way = input("\nWhere do you want to go? Enter Left or Right? ").lower()
        if way == 'left':
            # noinspection SpellCheckingInspection
            secondstage = input(
                "\nYou come to a lake. There is an island in the middle of lake. Do you want to 'swim' or 'wait' ?"). \
                lower()
            if secondstage == 'wait':
                door = input(
                    "\nYou arrived at island unharmed. Treasure is inside the 5 rooms : red, blue, yellow, golden, "
                    "white. "
                    "Which color do you choose ?").lower()
                if door in ['blue', 'white', 'red', 'golden']:
                    result = "Incorrect door chosen.You have attacked by Goons, Game over"
                elif door == 'yellow':
                    result = "\n************** You win !!! *************\n"
                else:
                    print("Enter valid characters.")
                    continue
                print(result)
                cont = input("Do you want to restart the game ? Enter Y or N ?").lower()
                if cont == 'y':
                    continue
                else:
                    print("See you again, Bye !!!")
                    break
            elif secondstage == 'swim':
                print("GAME OVER!")
                cont = input("Made wrong decision.\nDo you want to restart the game ? Enter Y or N ?").lower()
                if cont == 'y':
                    continue
                else:
                    print("See you again, Bye !!!")
                    break
        elif way == 'right':
            print('You fall into the hole. Game over!\n')
            cont = input("do you want to restart the game , enter y or n? ").lower()
            if cont == 'y':
                continue
            else:
                print("See you again, Bye !!!")
                break

        else:
            print("Enter the valid characters")
            cont = input("do you want to restart the game , enter y or n? ").lower()
            if cont == 'y':
                continue
            else:
                print("See you again, Have a Good day !!!")
                break


t_island()
