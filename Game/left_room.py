import hallway
import sys
sys.dont_write_bytecode = True #Don't produce pycache folder
def left_room_entry():
    area = "Left Room"
    inventory = {"Cell_key":True,"Torch":True,"Door_key":False,"Sword":False}
    action = str()
    
    while (action == 1 or action == ""):
        action = input("What do you want to do?\t1.Look around.\t2.Go back")
        action = int(action)
        if (action == 2):
            print ("You are now back in the hallway.")
            area = ("Hallway")
            hallway.hallway_options()
            print (area)
        elif (action == 1):
            print ("You look around. There is nothing here except empty shelves.")
        else:
            print ("This is not an option")
