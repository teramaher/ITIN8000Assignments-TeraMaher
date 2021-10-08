import datetime
import csv

#get all inputs - names color and birthday
fname = input("What is your first name?")
lname = input("What is your last name?")
color = input("What is your favorite color")
birthday = input("What is your B'day? (in MM/DD/YYYY) ")


#turn entered birthday into day element
birthdate = datetime.datetime.strptime(birthday,"%m/%d/%Y").date()
#the day it is today
today = datetime.date.today()
#calculation for subtraction between dates amount of days
daysold = (today - birthdate).days


#write name and color to text file
with open('UserName.txt', 'w') as f:
    f.write(lname + ',' + fname)
    f.write(color)
    # close file
    f.close()
#Write the user's age in days to a binary file named Days Old
#turn number into byte
daysbyte = daysold.to_bytes(5, 'little')
#open file and add it
fout = open('DaysOld.bin', 'wb')
fout.write(daysbyte)
#close file
fout.close()

#Add the user to a CSV file named UserData.csv in the order Last Name, First Name, Favorite Color, Days Old
with open('UserData.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow([lname, fname, color, daysold])
    #closing file
    csvfile.close()


