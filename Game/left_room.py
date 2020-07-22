# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:03:48 2020

@author: buddh
"""

area = "Left Room"
inventory = {"Cell_key":True,"Torch":True,"Door_key":False,"Sword":False}

action = str()

while (action == 1 or action == ""):
    action = input("What do you want to do?\t1.Look around.\t2.Go back")
    action = int(action)
    if (action == 2):
        print ("You are now back in the hallway.")
    elif (action == 1):
        print ("You look around. There is nothing here except empty shelves.")
        area = ("Hallway")
        print (area)
    else:
        print ("This is not an option")
