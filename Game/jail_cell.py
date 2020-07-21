# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:28:38 2020

@author: buddh
"""
area = "Jail Cell"
inventory = {"Cell_key":True,"Torch":False,"Door_key":False,"Sword":False}
while (area == "Jail Cell"):
    print ("What do you want to do?\n1.Look around.\n2.Wait for A while.")
    user_input = input()
    user_input = int(user_input)
    if (user_input == 1):
        print ("Looking around you can see:\n3.Locked door\n4.Rubble in a corner\n5.Barred off window.")
    elif (user_input == 2):
        print ("You wait in your cell for a while nothing has changed.")
        print ("What do you want to do?\n1.Look around.\n2.Wait for A while.")
    elif (user_input == 3 and inventory["Cell_Key"] == True):
        print ("The key fits perfectly and the door opens")
    elif (user_input == 3 and inventory["Cell_Key"] == False):
        print ("The door is locked. There is maybe a key around."
    else:
        print ("This is not an option")