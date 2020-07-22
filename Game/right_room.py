import hallway
import sys
sys.dont_write_bytecode = True #Don't produce pycache folder
def right_room_entry():
    area ="Right room"
    inventory = {"Cell_key":True,"Torch":True,"Door_key":False,"Sword":False}
    
    print("1.Skeleton")
    print("2.Armour Stand")
    print("3.Weapon rack")
    print("4.Go back")
    
    while (area == "Right room"):
        print (area)
        user_input = input("What do you want to do?")
        user_input = int(user_input)
        if (user_input == 1):
            print ("Checking the body reaveals a key.")
            inventory["Door_key"] = True
        elif (user_input == 2):
            print ("You come across a rusty set of armour. It hold no value")
        elif (user_input == 3):
            print ("You see a rack with just one sword that still is sharp.")
            inventory["Sword"] = True
        elif (user_input == 4):
            print ("You are now back in the hallway.")
            area = "End of Hallway"
            print (area)
            hallway.hallway_options()
        else:
            print ("This is not an option.")