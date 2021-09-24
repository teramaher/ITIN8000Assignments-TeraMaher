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

class Sides:
    def __init__(self):
        self.soupAmount = ran.randint(5, 10)
        self.saladAmount = ran.randint(5, 10)

    def soupCount(self):
        return self.soupAmount

    def saladCount(self):
        return self.saladAmount

    def subtract(self, entree):
        if entree == "empty":
            self.soupAmount = 0
            self.saladAmount = 0
        elif entree == "soup" and self.soupAmount > 0:
            self.soupAmount = self.soupAmount - 1
        elif entree == "salad" and self.saladAmount > 0:
            self.saladAmount = self.saladAmount - 1
        else:
            return False

    def outall(self):
        print("soup: " + str(self.soupAmount))
        print("salad: " + str(self.saladAmount))


class Wines:
    def __init__(self):
        self.merlotAmount = ran.randint(2, 5)
        self.charAmount = ran.randint(2, 5)
        self.noirAmount = ran.randint(2, 5)
        self.roseAmount = ran.randint(2, 5)

    def merlotCount(self):
        return self.merlotAmount

    def charCount(self):
        return self.charAmount

    def noirCount(self):
        return self.noirAmount

    def roseCount(self):
        return self.roseAmount

    def subtract(self, entree):
        if entree == "empty":
            self.merlotAmount = 0
            self.charAmount = 0
            self.noirAmount = 0
            self.roseAmount = 0
        if entree == "merlot" and self.merlotAmount > 0:
            self.merlotAmount = self.merlotAmount - 1
        elif entree == "chardonnay" and self.charAmount > 0:
            self.charAmount = self.charAmount - 1
        elif entree == "pinot noir" and self.noirAmount > 0:
            self.noirAmount = self.noirAmount - 1
        elif entree == "rose" and self.roseAmount > 0:
            self.roseAmount = self.roseAmount - 1
        else:
            return False

    def outall(self):
        print("Merlot: " + str(self.merlotAmount))
        print("Chardonnay: " + str(self.charAmount))
        print("Pinot Noir: " + str(self.noirAmount))
        print("Rose: " + str(self.roseAmount))


class Desserts:
    def __init__(self):
        self.flanAmount = ran.randint(1, 3)
        self.bruleeAmount = ran.randint(1, 3)
        self.mooseAmount = ran.randint(1, 3)
        self.cakeAmount = ran.randint(1, 3)

    def flanCount(self):
        return self.flanAmount

    def bruleeCount(self):
        return self.bruleeAmount

    def mooseCount(self):
        return self.mooseAmount

    def cakeCount(self):
        return self.cakeAmount

    def subtract(self, entree):
        if entree == "empty":
            self.flanAmount = 0
            self.bruleeAmount = 0
            self.mooseAmount = 0
            self.cakeAmount = 0
        elif entree == "flan" and self.flanAmount > 0:
            self.flanAmount = self.flanAmount - 1
        elif entree == "creme brulee" and self.bruleeAmount > 0:
            self.bruleeAmount = self.bruleeAmount - 1
        elif entree == "chocolate moose" and self.mooseAmount > 0:
            self.mooseAmount = self.mooseAmount - 1
        elif entree == "cheesecake" and self.cakeAmount > 0:
            self.cakeAmount = self.cakeAmount - 1
        else:
            return False

    def outall(self):
        print("Flan: " + str(self.flanAmount))
        print("Creme Brulee: " + str(self.bruleeAmount))
        print("Moose: " + str(self.mooseAmount))
        print("Cheesecake: " + str(self.cakeAmount))