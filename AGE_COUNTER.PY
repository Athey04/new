#=====================================================
    #Age Calculator With Birthday Countdown
#=====================================================

import datetime

year = int(input("Enter your DOB year (YYYY): "))
month = int(input("Enter your DOB month (MM): "))
day = int(input("Enter your DOB date (DD): "))


#Get todays date
today = datetime.date.today()
birthday = datetime.date(year,month,day)

def is_leap_year(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))


#Calculate current Age
age = today.year - birthday.year
if ((today.month, today.day)<(month,day)):
    age -= 1



next_birthday_year = today.year

#if birthday has already passed 
if ((today.month,today.day) <= (month,day)):
    next_birthday_year = today.year
else:
    next_birthday_year = today.year + 1
   
# Handle Feb 29 birthday
if month == 2 and day == 29:
# If next birthday year is NOT a leap year, use Feb 28
    if not (next_birthday_year % 4 == 0 and
            (next_birthday_year % 100 != 0 or next_birthday_year % 400 == 0)):
        next_birthday = datetime.date(next_birthday_year, 2, 28)
        
    else:
        next_birthday = datetime.date(next_birthday_year, 2, 29)
else:
    next_birthday = datetime.date(next_birthday_year, month, day)
     


#Calculate days remaining for the upcoming birthday
difff = (next_birthday - today).days


print("\n--- Results ---")
#Prints your current age
print(f"Your current age is: {age}")

if (today == next_birthday):
    print("🎉🎉Happy Birthday!🥳🎂🎂")
else:
    print(f"Your Birthday is in: {difff} days")




