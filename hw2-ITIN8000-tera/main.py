#imports
import menu as menu
import re
import os
import random as ran
#assign entrees
entrees = menu.Entrees()
wines = menu.Wines()
#assign sides
sides = menu.Sides()
#assign desserts
desserts = menu.Desserts()
#assign wines
wines = menu.Wines()
#print welcome
print("Hello! Welcome to my resturant! Go through by picking the number you want to do")
#ask what role they want
role = input("What is your role? Your options are \n1. Waiter \n2. Customer \n3. Manager\n4. End Program\n 1, 2, 3, or 4:")
#loop through different rolls
while role != "4":
    #role 1, a employee

    if role == "1":
        # ask for whole menu or different categories
        action = input("What do you want to do? Read out the: \n1. Whole Menu \n2. Entree \n3. Wines \n4. Sides \n5. Desserts?\n1, 2, 3, or 4:")
        # print all of category by calling outall for everyone
        if action == "1":
            entrees.outall()
            sides.outall()
            desserts.outall()
            wines.outall()
        # print all of the chosen category
        if action == "2":
            entrees.outall()
        if action == "3":
            wines.outall()
        if action == "4":
            sides.outall()
        if action == "5":
            desserts.outall()

    #role 2, a customer

    #order choice
    #loop if there is none left of order and they want to order
    #order from menu

    #ask customer what they want from menu

    #sort the input with regex by checking if type is in there

    #check if entree is empty or none left and subtract if

    #check if side is empty or none left and subtract if

    #check if wine is empty or none left and subtract if

    #check if dessert is empty or none left and subtract if

    #random choice




    #roll 3 the manager
    if role == "3":
        #ask if they want to open or close
        action = input("What do you want to do? Read \n1. Close\n2. Open?\n1 or 2:")
        # to close:
        if action == "1":
            #prints out all of menu
            entrees = menu.Entrees()
            sides = menu.Sides()
            desserts = menu.Desserts()
            wines = menu.Wines()
            # sets all menu items to zero with subtract
            entrees.subtract("empty")
            sides.subtract("empty")
            desserts.subtract("empty")
            wines.subtract("empty")
        #to open:
        if action == "2":
            print("Restarting...")
            # restart the menu file
            os.system("python menu.py")
            # restart the main file
            os.system("python main.py")
            exit()


    #asks what role you want
    role = input("What is your role? Your options are \n1. Waiter \n2. Customer \n3. Manager\n4. End Program\n 1, 2, or 3:")
