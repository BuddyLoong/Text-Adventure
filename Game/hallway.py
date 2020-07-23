import left_room, right_room,middle_room, jail_cell
import sys
sys.dont_write_bytecode = True #Don't produce pycache folder
inventory = {"Cell_key":False,"Torch":False,"Door_key":False,"Sword":False}
action1 = str()
inventory = {"Cell_key":True,"Torch":False, "Door_key":False} #add key1, key2 and sword later
def hallway_options(inventory):
    area = "End of Hallway"
    while(area == "End of Hallway"):
        print("You see three doors. Which do you want to go through?")   
        action2 = input("Left Door\tMiddle Door\tRight Door\n(l\\m\\r)\n")
        if(action2 == "l"):
            print("You enter the left door")
            area = "Left Room"
            left_room.left_room_entry(inventory)
            return inventory
            #PLACEHOLDER: enter left_room.py here
        elif (action2 == "m" and inventory["Door_key"] == False):
            print("The Door is locked.\nMaybe one of the other rooms have the key.")
        elif (action2 == "m" and inventory["Door_key"] == True):
            print("You enter the middle room")
            area = "Middle Room"
            middle_room.middle_room_entry(inventory)
            return inventory
            #PLACEHOLDER: enter middle_room.py here

        elif (action2 == "r"):
            print("You enter the right room")
            area = "Right Room"
            right_room.right_room_entry(inventory)
            return inventory
            #PLACEHOLDER: enter right_room.py here
        else:
            print("That is not an option")
    
def hallway_entry(inventory):
    
    # inventory = {"Cell_key":True,"Torch":False, "Door_key":False} #add key1, key2 and sword later
    area = "Hallway" #Change to Jail cell or room
    print("You step into a dark hallway")
    # user_input = input("What do you want to do?")
    # user_input = int(user_input)
    
    
    while(area == "Hallway"):
        print("1.Go down the dark hallway.\t2.Grab torch.\t3.Go back into the jail cell.")
        print("What do you want to do?")
        action1 = input("(1\\2\\3)\n")
        action1 = int(action1)
        
        if(action1 == 1 and inventory["Torch"] == False):
            print("It's too dark.")
        elif(action1 == 2 and inventory["Torch"] == False):
            print("You grabbed the torch!\nWOW, so bright")
            inventory["Torch"] = True
        elif(action1 == 2 and inventory["Torch"] == True):
            print("You are already holding the torch...")
        elif(action1 == 3):
            print("You go back into the jail cell")
            area = "Jail cell"
        elif(action1 == 1 and inventory["Torch"] == True):
            print("You walk down the hallway")
            area = "End of hallway"

        else:
            print("That is not an option")

    if(action1 == 3):
        #PLACEHOLDER: Go back to room
        print("You are back in your jail cell, what do you want to do?")
        print("Exiting now")
        jail_cell.jail_cell_return(inventory)
        return inventory
    else:
        print("You are at the end of the hallway")
        area = "End of hallway"
        hallway_options(inventory)
        return inventory


    
