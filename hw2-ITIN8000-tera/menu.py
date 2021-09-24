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
            self.chickenAmount = self.chickenAmount - 1
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
    #outputs a list version of what is left
    def listRep(self):
        result = []
        #takes amount of entrees left and then adds to list as it goes through
        for i in range(self.vegAmount):
            result.append("vegetarian")
        for i in range(self.beefAmount):
            result.append("beef")
        for i in range(self.chickenAmount):
            result.append("chicken")
        return result

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

    def subtract(self, entree):
        if entree == "empty":
            self.soupAmount = 0
            self.saladAmount = 0
        elif entree == "soup" and self.soupAmount > 0:
            self.soupAmount = self.soupAmount - 1
            return False
        elif entree == "salad" and self.saladAmount > 0:
            self.saladAmount = self.saladAmount - 1
            return False
        else:
            return True
    #outputs a list version of what is left

    def listRep(self):
        result = []
        #takes amount of sides left and then adds to list as it goes through
        for i in range(self.soupAmount):
            result.append("soup")
        for i in range(self.saladAmount):
            result.append("salad")
        return result

    def outall(self):
        print("soup: " + str(self.soupAmount))
        print("salad: " + str(self.saladAmount))


class Wines:
    def __init__(self):
        self.merlotAmount = ran.randint(2, 5)
        self.charAmount = ran.randint(2, 5)
        self.noirAmount = ran.randint(2, 5)
        self.roseAmount = ran.randint(2, 5)

    def subtract(self, entree):
        if entree == "empty":
            self.merlotAmount = 0
            self.charAmount = 0
            self.noirAmount = 0
            self.roseAmount = 0
        if entree == "merlot" and self.merlotAmount > 0:
            self.merlotAmount = self.merlotAmount - 1
            return False
        elif entree == "chardonnay" and self.charAmount > 0:
            self.charAmount = self.charAmount - 1
            return False
        elif entree == "pinot noir" and self.noirAmount > 0:
            self.noirAmount = self.noirAmount - 1
            return False
        elif entree == "rose" and self.roseAmount > 0:
            self.roseAmount = self.roseAmount - 1
            return False
        else:
            return True

    #outputs a list version of what is left
    def listRep(self):
        result = []
        #takes amount of wines left and then adds to list as it goes through
        for i in range(self.merlotAmount):
            result.append("merlot")
        for i in range(self.charAmount):
            result.append("chardonnay")
        for i in range(self.noirAmount):
            result.append("pinot noir")
        for i in range(self.roseAmount):
            result.append("rose")
        return result

    def outall(self):
        print("merlot: " + str(self.merlotAmount))
        print("chardonnay: " + str(self.charAmount))
        print("pinot Noir: " + str(self.noirAmount))
        print("rose: " + str(self.roseAmount))


class Desserts:
    def __init__(self):
        self.flanAmount = ran.randint(1, 3)
        self.bruleeAmount = ran.randint(1, 3)
        self.mooseAmount = ran.randint(1, 3)
        self.cakeAmount = ran.randint(1, 3)

    def subtract(self, entree):
        if entree == "empty":
            self.flanAmount = 0
            self.bruleeAmount = 0
            self.mooseAmount = 0
            self.cakeAmount = 0
        elif entree == "flan" and self.flanAmount > 0:
            self.flanAmount = self.flanAmount - 1
            return False
        elif entree == "creme brulee" and self.bruleeAmount > 0:
            self.bruleeAmount = self.bruleeAmount - 1
            return False
        elif entree == "chocolate moose" and self.mooseAmount > 0:
            self.mooseAmount = self.mooseAmount - 1
            return False
        elif entree == "cheesecake" and self.cakeAmount > 0:
            self.cakeAmount = self.cakeAmount - 1
            return False
        else:
            return True

        # outputs a list version of what is left
    def listRep(self):
        result = []
        # takes amount of desserts left and then adds to list as it goes through
        for i in range(self.flanAmount):
            result.append("flan")
        for i in range(self.bruleeAmount):
            result.append("creme brulee")
        for i in range(self.mooseAmount):
            result.append("chocolate moose")
        for i in range(self.cakeAmount):
            result.append("cheesecake")
        return result

    def outall(self):
        print("flan: " + str(self.flanAmount))
        print("creme Brulee: " + str(self.bruleeAmount))
        print("moose: " + str(self.mooseAmount))
        print("cheesecake: " + str(self.cakeAmount))
