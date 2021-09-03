from datetime import datetime
#set up date
today = datetime.now()
#take the month, day, and year from date
month_name = today.strftime("%B")
month_number = today.month
day_number = today.day
year_number = today.year

#figure out the [th/nd/st/rd] of the day
#if 1, 21, or 31 its st
if day_number == 1 or 21 or 31:
    suffix = "st"
#else if 2 or 22 its nd
elif day_number == 2 or 22:
    suffix = "nd"
#else if 3 or 23 its rd
elif day_number == 3 or 23:
    suffix = "rd"
#else its th
else:
    suffix = "th"

#calculate product of the month and day
productCalc = month_number * day_number
#figure out if product is odd or even number
#if the remainder is 0 when devided by two its even
if productCalc % 2 == 0:
    day_type = "even"
#if the remainder is not its odd
else:
    day_type = "odd"

#print out the first sentence with different components
print("Hello. Todays Date is", month_name, str(day_number) + suffix, "of", str(year_number) + ". The product of the month and day is", str(productCalc)+ ", which is an", day_type, "number.\n")

#print out If you counted the days this month so far you would have
print("If you counted the days this month so far you would have")

n=1
#while loop till the amount of days is 0
while n <= day_number:
    #print out the number
    print(n)
    n = n + 1
#print out 'days'
print("days")

