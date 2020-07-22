# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:28:38 2020

@author: buddh
"""

def start_game():
    area = "Jail Cell"
    inventory = {"Cell_key":False,"Torch":False,"Door_key":False,"Sword":False}

    action = str()
    
    while (action == 2 or action == ""):
        action = input("What do you want to do?\t1.Look around.\t2.Wait for A while")
        action = int(action)
        if (action == 2):
            print ("You wait in your cell for a while nothing has changed.")
        elif (action == 1):
            print ("You look around.")
            break 
        else:
            print ("This is not an option")
    print ("Got out of the first while loop.")
            
    while (area == "Jail Cell" and action == 1):
        print ("Looking around you can see:\t3.Locked door\t4.Rubble in a corner\t5.Barred off window.")
    
        user_input = input()
        user_input = int(user_input)
        if (user_input == 3 and inventory["Cell_key"] == True):
            print ("The key fits perfectly and the door opens")
            area = "Hallway"
        elif (user_input == 3 and inventory["Cell_key"] == False):
            print ("The door is locked.")
        elif (user_input == 4 and inventory["Cell_key"] == False):
            print("While searching through the rubble you find a rusty key.")
            inventory["Cell_key"] = True
        elif (user_input == 4 and inventory["Cell_key"] == True):
            print ("You have already found the key.")
        elif (user_input == 5):
            print ("You can see outside through the window. Sadly the bars are stopping you from going through.")
            
        else:
            print ("This is not an option")