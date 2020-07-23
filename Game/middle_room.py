import sys, hallway
sys.dont_write_bytecode = True #Don't produce pycache folder
def middle_room_entry(inventory):
    
    area = "Middle Room"
    print ("You enter a long hallway. \nAt the end of the hallway you can see an exit...\nHowever, there is a troll blocking the exit")
    print ("What do you want to do")
    print ("1.Look around")
    print ("2.Attack Troll")
    print ("3.Throw Torch at the Troll")
    print ("4.Go back")
    user_action = input()
    user_action = int(user_action)

    while (user_action == 1):
        if (user_action == 1):
            print ("You look around. There is only an exit and a troll.")
            print ("What do you want to do")
            print ("1.Look around")
            print ("2.Attack Troll")
            print ("3.Throw Torch at the Troll")
            print ("4.Go back")
            break
        else:
            print ("This is not an option")
   
    if (user_action == 2 and inventory["Sword"] == False):
        print ("You attack the troll without a weapon.\nYou Died")
        print ("Game Over")
    elif (user_action == 2 and inventory["Sword"] == True):
        print ("You attack the troll with the sword you have obtained.\nThe Troll dies")
        print ("Congrates you have completed Text-Adventure.")
    elif (user_action == 3):
        print ("You throw the torch at the troll.\nThis enrage the troll and it attacks you.\nYou Died.")
        print ("Game Over")
    elif (user_action == 4):
        print ("You go back through the doorway")
        area = "End of Hallway"
        hallway.hallway_options()

#Create a function for if the player has the Sword
#Create a function for if the player does not have the Sword