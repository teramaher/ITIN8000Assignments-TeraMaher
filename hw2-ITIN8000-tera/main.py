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
        action = input("What do you want to do? Read out the: \n1. Whole Menu \n2. Entree \n3. Wines \n4. Sides \n5. Desserts\n1, 2, 3, 4, or 5:")
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
    if role == "2":
        #order choice
        action = input("What do you want to do? \n1. Order food \n2. random choice?\n1 or 2:")
        if action == "1":
            reorder = "1"
            # loop if there is none left of order and they want to order
            while reorder == "1":
            #order from menu
            #ask customer what they want from menu
                order = input("please enter what you want from menu")
                #sort the input with regex by checking if type is in there
                entree_order = re.findall(r"\bchicken\b|\bbeef\b|\bvegetarian\b", order.lower())
                side_order = re.findall(r"\bsoup\b|\bsalad\b", order.lower())
                wine_order = re.findall(r"\bmerlot\b|\bchardonnay\b|\bpinot noir\b|\brose\b", order.lower())
                dessert_order = re.findall(r"\bflan\b|\bcreme brulee\b|\bchocolate moose\b|\bcheesecake\b", order.lower())
                print("thank you for ordering!")
                reorder = "2"
                #check if entree is empty or none left and subtract if
                if entree_order and entrees.subtract(entree_order[0]):
                    reorder = input("sorry we are out of " + entree_order[0] + ", do you want to reorder? 1. yes 2. no:")
                #check if side is empty or none left and subtract if
                if side_order and sides.subtract(side_order[0]):
                    reorder = input("sorry we are out of " + side_order[0] + ", do you want to reorder? 1. yes 2. no:")
                #check if wine is empty or none left and subtract if
                if wine_order and wines.subtract(wine_order[0]):
                    reorder = input("sorry we are out of " + wine_order[0] + ", do you want to reorder? 1. yes 2. no:")
                #check if dessert is empty or none left and subtract if
                if dessert_order and desserts.subtract(dessert_order[0]):
                    reorder = input("sorry we are out of " + dessert_order[0]+", do you want to reorder? 1. yes 2. no:")

        #random choice
        if action == "2":
            print("your dinner will be:")
            if entrees.listRep():
                ran_entree = ran.choice(entrees.listRep())
                entrees.subtract(ran_entree)
                print(ran_entree)

            if sides.listRep():
                ran_side = ran.choice(sides.listRep())
                sides.subtract(ran_side)
                print(ran_side)

            if wines.listRep():
                ran_wine = ran.choice(wines.listRep())
                wines.subtract(ran_wine)
                print(ran_wine)

            if desserts.listRep():
                ran_dessert = ran.choice(desserts.listRep())
                desserts.subtract(ran_dessert)
                print(ran_dessert)

            #print("Your order for tonight is: " + ran_entree+",", ran_side+",", ran_wine+",",ran_dessert)

    #roll 3 the manager
    if role == "3":
        #ask if they want to open or close
        action = input("What do you want to do? \n1. Close\n2. Open?\n1 or 2:")
        # to close:
        if action == "1":
            #prints out all of menu
            print(entrees.outall())
            print(sides.outall())
            print(wines.outall())
            print(desserts.outall())
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
    role = input("What is your role? Your options are \n1. Waiter \n2. Customer \n3. Manager\n4. End Program\n 1, 2, 3, or 4:")
