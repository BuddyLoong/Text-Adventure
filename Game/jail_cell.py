import hallway   
def start_game():

    inventory = {"Cell_key":False,"Torch":False,"Door_key":False,"Sword":False}
    area = "Jail Cell"
    
    action = str() 
    
        #or is used if one of the requirements is reached
        #while statement is used to run code the same code until the value is equal to the requirement
    while (action == 2 or action == ""):
            action = input("What do you want to do?\t1.Look around.\t2.Wait for A while")
            action = int(action)
            if (action == 2):
                print ("You wait in your cell for a while nothing has changed.")
            elif (action == 1):
                print ("You look around.")
        #break is used to stop a line of code from being used more than once
                break 
            else:
                print ("This is not an option")
                print ("Got out of the first while loop.")
        #and is used if another requiremnt is needed
    while (area == "Jail Cell" and action == 1):
            print ("Looking around you can see:\t3.Locked door\t4.Rubble in a corner\t5.Barred off window.")
            user_input = input()
            user_input = int(user_input)
        #and is used here to see if both requiremnts are met.
        #each statement has a True and False which will determine which print will show.
            if (user_input == 3 and inventory["Cell_key"] == True):
                print ("The key fits perfectly and the door opens")
                area = "Hallway"
                hallway.hallway_entry()
            elif (user_input == 3 and inventory["Cell_key"] == False):
                print ("The door is locked.")
            elif (user_input == 4 and inventory["Cell_key"] == False):
                print("While searching through the rubble you find a rusty key.")
                inventory["Cell_key"] = True
            elif (user_input == 4 and inventory["Cell_key"] == True):
                print ("You have already found the key.")
            elif (user_input == 5):
                print ("You can see outside through the window. Sadly the bars are stopping you from going through.")
        #The else statement is used if the user does not follow any of the options. For example, type 5
            else:
                print ("This is not an option")

def jail_cell_return():        
    inventory = {"Cell_key":True,"Torch":False,"Door_key":False,"Sword":False}
    area = "Jail Cell"
    
    action = str()
   
    while (action == 2 or action == ""):
            action = input("What do you want to do?\t1.Look around.\t2.Wait for A while")
            action = int(action)
            if (action == 2):
                print ("You wait in your cell for a while nothing has changed.")
            elif (action == 1):
                print ("You look around.")
        #break is used to stop a line of code from being used more than once
                break 
            else:
                print ("This is not an option")
    while (area == "Jail Cell" and action == 1):
            print ("Looking around you can see:\t3.Locked door\t4.Rubble in a corner\t5.Barred off window.")
            user_input = input()
            user_input = int(user_input)
        #and is used here to see if both requiremnts are met.
        #each statement has a True and False which will determine which print will show.
            if (user_input == 3 and inventory["Cell_key"] == True):
                print ("The key fits perfectly and the door opens")
                area = "Hallway"
                hallway.hallway_entry()
            elif (user_input == 3 and inventory["Cell_key"] == False):
             print ("The door is locked.")
            elif (user_input == 4 and inventory["Cell_key"] == False):
             print("While searching through the rubble you find a rusty key.")
            inventory["Cell_key"] = True
            elif (user_input == 4 and inventory["Cell_key"] == True):
             print ("You have already found the key.")
            elif (user_input == 5):
            print ("You can see outside through the window. Sadly the bars are stopping you from going through.")
    #The else statement is used if the user does not follow any of the options. For example, type 5
            else:
            print ("This is not an option")
