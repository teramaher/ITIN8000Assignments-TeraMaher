import random as ran
#class entree
class Entrees:
    #define entree numbers with randint in init function
    def __init__(self):
        self.vegAmount = ran.randint(1, 6)
        self.beefAmount = ran.randint(1, 6)
        self.chickenAmount = ran.randint(1, 6)

    #SUBTRACT function

    def subtract(self, entree):
        # check if it is empty request
        if entree == "empty":
            self.vegAmount = 0
            self.beefAmount = 0
            self.chickenAmount = 0
        # else if check if entered plate has one left
        elif entree == "chicken" and self.chickenAmount > 0:
            # subtract one
            self.chickenAmount = self.chickenAmount - 1
            # return false
            return False
        elif entree == "beef" and self.beefAmount > 0:
            self.beefAmount = self.beefAmount - 1
            return False
        elif entree == "vegetarian" and self.vegAmount > 0:
            self.vegAmount = self.vegAmount - 1
            return False
        # else return true
        else:
            return True

#OUTALL function
#print plate and the amount of plate left
    def outall(self):
        print("chicken: " + str(self.vegAmount))
        print("beef: " + str(self.beefAmount))
        print("vegetarian: " + str(self.vegAmount))



#class side

#define side numbers with randint in init function

#SUBTRACT function
#check if it is empty request
#else if check if entered plate has one left
#subtract one
#return false
#else return true

#OUTALL function
#print plate and the amount of plate left




#class wine
#define wine numbers with randint in init function

#SUBTRACT function
#check if it is empty request
#else if check if entered plate has one left
#subtract one
#return false
#else return true

#OUTALL function
#print plate and the amount of plate left





#class dessert
#define dessert numbers with randint in init function

#SUBTRACT function
#check if it is empty request
#else if check if entered plate has one left
#subtract one
#return false
#else return true

#OUTALL function
#print plate and the amount of plate left