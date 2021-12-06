import csv
rows = []
from datetime import datetime
import pandas as pd
import random as ran
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy_garden.mapview import MapView

global hours
# the day it is within the csv file aka 0-monday = 1 on csv file
day = datetime.today().weekday() * 2 + 1


def calcColor(StoreOpen, StoreClose):
    #if the store is not closed for the day
    if StoreOpen != '' and StoreClose != '':
        # turn csv input to a datetime object
        StoreOpen = datetime.strptime(StoreOpen, '%I:%M %p').time()  # convert to a time format. 06:00:00
        StoreClose = datetime.strptime(StoreClose, '%I:%M %p').time()  # convert to a time format. #22:00:00
        #if it is 11-2 then it is the first icon (sun)
        if StoreClose.hour == 11 or StoreClose.hour == 12:
            return "1.png"
        if StoreClose.hour == 13 or StoreClose.hour == 14:
            return "1.png"
        # if it is 3-4 then it is the second icon (sun)
        if StoreClose.hour == 15 or StoreClose.hour == 16:
            return "2.png"
        # if it is 5-6 then it is the third icon (half moon)
        if StoreClose.hour == 17 or StoreClose.hour == 18:
            return "3.png"
        # if it is 7-8 then it is the fourth icon (moon)
        if StoreClose.hour == 19 or StoreClose.hour == 20:
            return "4.png"
        # if it is 9-12 then it is the fifth icon (moon and star)
        if StoreClose.hour == 21 or StoreClose.hour == 22 or StoreClose.hour == 23 or StoreClose.hour == 24:
            return "5.png"


    return "1.png"



#calculates if the store is open
def calcOpen(StoreOpen, StoreClose):
    #the current time
    tnow = datetime.now().time()
    #if the store is open (not empty)
    if StoreOpen != '' or StoreClose != '':
        #set string input to datetime
        StoreOpen = datetime.strptime(StoreOpen, '%I:%M %p').time()  # convert to a time format. 06:00:00
        StoreClose = datetime.strptime(StoreClose, '%I:%M %p').time()  # convert to a time format. #22:00:00
        #if the current time is after the open and before the close
        if (StoreOpen <= tnow and StoreClose >= tnow):
            return True
        else:
            return False
    return False

#give the user a random resturant to look at
def randomResturant(reslist, day):
    #the set up for open stores
    potential = []
    #for all in current list, check if open
    for i in reslist:
        #use calc open to see if open then add
        if calcOpen(i[day],i[day + 1]):
            potential.append(i)
    # if none open, no coffee shops are open
    if len(potential) == 0:
        return "no coffee shops open"
    #else return random from the list
    else:
        return (ran.choice(potential))[0]



#read through the file and create array for each cafe
with open("coffee-hours.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)


#number input: 1= monday, 3=tuesday, 5=wednesday, 7=thursday, 9=friday, 11=saturday, 13=sunday
#randomResturant(rows, 3)
#print(datetime.today().weekday() * 2 + 1)
#print(calcColor(rows[2][1], rows[2][2]))
#print(rows[2][3])

#the gui for the application
class SayHello(App):
    def build(self):



        #locColor = calcColor(rows[2][day], rows[2][day+1])

        #creating the window
        self.window = GridLayout()
        self.window.clearcolor = (1, 1, 1, 1)
        #one column lay out
        self.window.cols = 1

        # the edges of the screen going to 90 of the left and right and 99% of top bottom
        self.window.size_hint = (0.9, 0.99)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #intro sentence
        self.greeting = Label(text="Welcome to Teras omaha coffee recs!",
                              font_size=20,
                              )
        self.window.add_widget(self.greeting)

        #adding the image of the key
        self.window.add_widget(Image(source='Key.png', size_hint=(1,1)))



        #assigning all 20 of the pins
        self.loc0button = Button(size=(40,50), size_hint=(.5, .5), background_normal= calcColor(rows[0][day], rows[0][day+1]), pos=(405, 395), background_down ="6.png")
        self.loc1button = Button(size=(40,50), size_hint=(1, 0.5), background_normal= calcColor(rows[1][day], rows[1][day+1]), pos=(600, 350), background_down ="6.png")
        self.loc2button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[2][day], rows[2][day + 1]), pos=(690, 250), background_down ="6.png")
        self.loc3button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[3][day], rows[3][day + 1]), pos=(620, 250), background_down ="6.png")
        self.loc4button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[4][day], rows[4][day + 1]), pos=(460, 300), background_down ="6.png")
        self.loc5button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[5][day], rows[5][day + 1]), pos=(650, 245), background_down ="6.png")


        self.loc7button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[7][day], rows[7][day + 1]), pos=(390, 180), background_down ="6.png")
        self.loc8button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[8][day], rows[8][day + 1]), pos=(650, 230), background_down ="6.png")
        self.loc9button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[9][day], rows[9][day + 1]), pos=(260, 220), background_down ="6.png")
        self.loc10button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[10][day], rows[10][day + 1]), pos=(370, 180), background_down ="6.png")
        self.loc11button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[11][day], rows[11][day + 1]), pos=(590, 250), background_down ="6.png")
        self.loc12button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[12][day], rows[12][day + 1]), pos=(100, 280), background_down ="6.png")
        self.loc13button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[13][day], rows[13][day + 1]), pos=(540, 310), background_down ="6.png")
        self.loc14button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[14][day], rows[14][day + 1]), pos=(540, 250), background_down ="6.png")
        self.loc15button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[15][day], rows[15][day + 1]), pos=(450, 230), background_down ="6.png")
        self.loc16button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[16][day], rows[16][day + 1]), pos=(580, 300), background_down ="6.png")
        self.loc17button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[17][day], rows[17][day + 1]), pos=(690, 310), background_down ="6.png")
        self.loc18button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[18][day], rows[18][day + 1]), pos=(690, 250), background_down ="6.png")
        self.loc19button = Button(size=(40,50), size_hint=(1, 0.5), background_normal=calcColor(rows[19][day], rows[19][day + 1]), pos=(620, 250), background_down ="6.png")
        #the image the pin goes on
        self.mapimage = Image(source='locations3.png', size=(100, 90), size_hint=(10,5))


        #when clicking the buttons, the different press pops up and is assigned to the image for all 20
        self.loc0button.bind(on_press=self.resturantcall)
        self.mapimage.add_widget(self.loc0button)
        self.loc1button.bind(on_press=self.resturant1call)
        self.mapimage.add_widget(self.loc1button)
        self.loc2button.bind(on_press=self.resturant2call)
        self.mapimage.add_widget(self.loc2button)
        self.loc3button.bind(on_press=self.resturant3call)
        self.mapimage.add_widget(self.loc3button)
        self.loc4button.bind(on_press=self.resturant4call)
        self.mapimage.add_widget(self.loc4button)
        self.loc5button.bind(on_press=self.resturant5call)
        self.mapimage.add_widget(self.loc5button)

        self.loc7button.bind(on_press=self.resturant7call)
        self.mapimage.add_widget(self.loc7button)
        self.loc8button.bind(on_press=self.resturant8call)
        self.mapimage.add_widget(self.loc8button)
        self.loc9button.bind(on_press=self.resturant9call)
        self.mapimage.add_widget(self.loc9button)
        self.loc10button.bind(on_press=self.resturant10call)
        self.mapimage.add_widget(self.loc10button)
        self.loc11button.bind(on_press=self.resturant11call)
        self.mapimage.add_widget(self.loc11button)
        self.loc12button.bind(on_press=self.resturant12call)
        self.mapimage.add_widget(self.loc12button)
        self.loc13button.bind(on_press=self.resturant13call)
        self.mapimage.add_widget(self.loc13button)
        self.loc14button.bind(on_press=self.resturant14call)
        self.mapimage.add_widget(self.loc14button)
        self.loc15button.bind(on_press=self.resturant15call)
        self.mapimage.add_widget(self.loc15button)
        self.loc16button.bind(on_press=self.resturant16call)
        self.mapimage.add_widget(self.loc16button)
        self.loc17button.bind(on_press=self.resturant17call)
        self.mapimage.add_widget(self.loc17button)
        self.loc18button.bind(on_press=self.resturant18call)
        self.mapimage.add_widget(self.loc18button)
        self.loc19button.bind(on_press=self.resturant19call)
        self.mapimage.add_widget(self.loc19button)

        # add the image to the screen
        self.window.add_widget(self.mapimage)
        #self.button.add_widget()
        # label for prompts but also the different information
        self.greeting = Label(text="click a square for more info!", font_size = 20)
        self.window.add_widget(self.greeting)

        #the button that pulls up random shop
        self.button = Button(text="Pick Random coffee shop", size=(20,70), background_color= '#ad6d2f' )
        #self.button.add_widget()
        #callback that changes the text
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)





        return self.window
    #gets the random coffee shop method and asks if you want to go
    def callback(self, instance):
        #row is the list of resturants and day is the corresponding column name
        self.greeting.text = "Random coffee shop:" + randomResturant(rows, day)
    # all of the different calls for the different information
    def resturantcall(self, instance):
        self.greeting.text = rows[0][0] + " is open today from: " + rows[0][day] + " - " + rows[0][day + 1]

    def resturant1call(self, instance):
        self.greeting.text = rows[1][0] + " is open today from: " + rows[1][day] + " - " + rows[1][day + 1]

    def resturant2call(self, instance):
        self.greeting.text = rows[2][0] + " is open today from: " + rows[2][day] + " - " + rows[2][day + 1]

    def resturant3call(self, instance):
        self.greeting.text = rows[3][0] + " is open today from: " + rows[3][day] + " - " + rows[3][day + 1]

    def resturant4call(self, instance):
        self.greeting.text = rows[4][0] + " is open today from: " + rows[4][day] + " - " + rows[4][day + 1]

    def resturant5call(self, instance):
        self.greeting.text = rows[5][0] + " is open today from: " + rows[5][day] + " - " + rows[5][day + 1]

    def resturant6call(self, instance):
        self.greeting.text = rows[6][0] + " is open today from: " + rows[6][day] + " - " + rows[6][day + 1]

    def resturant7call(self, instance):
        self.greeting.text = rows[7][0] + " is open today from: " + rows[7][day] + " - " + rows[7][day + 1]

    def resturant8call(self, instance):
        self.greeting.text = rows[8][0] + " is open today from: " + rows[8][day] + " - " + rows[8][day + 1]

    def resturant9call(self, instance):
        self.greeting.text = rows[9][0] + " is open today from: " + rows[9][day] + " - " + rows[9][day + 1]

    def resturant10call(self, instance):
        self.greeting.text = rows[10][0] + " is open today from: " + rows[10][day] + " - " + rows[10][day + 1]

    def resturant11call(self, instance):
        self.greeting.text = rows[11][0] + " is open today from: " + rows[11][day] + " - " + rows[11][day + 1]

    def resturant12call(self, instance):
        self.greeting.text = rows[12][0] + " is open today from: " + rows[12][day] + " - " + rows[12][day + 1]

    def resturant13call(self, instance):
        self.greeting.text = rows[13][0] + " is open today from: " + rows[13][day] + " - " + rows[13][day + 1]

    def resturant14call(self, instance):
        self.greeting.text = rows[14][0] + " is open today from: " + rows[14][day] + " - " + rows[14][day + 1]

    def resturant15call(self, instance):
        self.greeting.text = rows[15][0] + " is open today from: " + rows[15][day] + " - " + rows[15][day + 1]

    def resturant16call(self, instance):
        self.greeting.text = rows[16][0] + " is open today from: " + rows[16][day] + " - " + rows[16][day + 1]

    def resturant17call(self, instance):
        self.greeting.text = rows[17][0] + " is open today from: " + rows[17][day] + " - " + rows[17][day + 1]

    def resturant18call(self, instance):
        self.greeting.text = rows[18][0] + " is open today from: " + rows[18][day] + " - " + rows[18][day + 1]

    def resturant19call(self, instance):
        self.greeting.text = rows[19][0] + " is open today from: " + rows[19][day] + " - " + rows[19][day + 1]


#runs the main program
if __name__ ==  "__main__":
    SayHello().run()