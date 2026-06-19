print ("Welcome to the Interactive Personal Data Collector!")
print (sep="!")

name = str(input("Please enter your Name:"))
age = int(input("Please enter your age:"))
height = float(input("Please enter your height in meters:"))
favourite_number = int(input("Please enter your Favourite Number:"))

print (sep ="!")

print ("Thankyou! Here is your information that we collected.")

print (sep ="!")

print ("Name:",(name),"( Type:",type(name),"Memory Address:",id(name),")")
print ("Age:",(age),"( Type:",type(age),"Memory Address:",id(age),")")
print ("Height:",(height),"( Type:",type(height),"Memory Address:",id(height),")")
print ("Favourite_Number:",(favourite_number),"( Type:",type(favourite_number),"Memory Address:",id(favourite_number),")")

print (sep ="!")

print ("your Birth year is approximatealy:",2026-age,"( based on your age of",int(age),")")

print (sep ="!")

print ("Thank you for using the Personal Data Collector,Good_bye!")
