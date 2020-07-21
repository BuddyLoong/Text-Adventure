import sys

inventory = {"Cell_key":True,"Torch":False, "Door_key":False} #add key1, key2 and sword later
action1 = str()
area = "Hallway" #Change to Jail cell or room
print("You step into a dark hallway")

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
        #PLACEHOLDER: Link back to text_adventure.py
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
    sys.exit()
else:
    print("You are at the end of the hallway")
    area = "End of hallway"

while(area == "End of hallway"):
    print("You see three doors. Which do you want to go through?")   
    action2 = input("Left Door\tMiddle Door\tRight Door\n(l\\m\\r)\n")
    if(action2 == "l"):
        print("You enter the left door")
        area = "Left Room"
        #PLACEHOLDER: enter left_room.py here
    elif(action2 == "m"):
        print("You enter the middle room")
        area = "Middle Room"
        #PLACEHOLDER: enter middle_room.py here
    elif(action2 == "r"):
        print("You enter the right room")
        area = "Right Room"
        #PLACEHOLDER: enter right_room.py here
    else:
        print("That is not an option")

    

