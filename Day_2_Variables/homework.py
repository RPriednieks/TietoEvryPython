import datetime

#Exercise 1
username = input("What is your name? ")
age = input(f"How old are you, {username}? ")
years = 100 - int(age)
print(f"Mmm, its {years} till 100!")
currentYear = datetime.datetime.now().year
milestone = currentYear + years
print(f"You will be 100 years old at year {milestone}!")

#Exercise 2
width = float(input("Enter width: "))
length = float(input("Enter length: "))
height = float(input("Enter height: "))
volume = width * length * height
print(f"Volume is {volume} m3")

#Exercise 3
celsius = float(input("Enter temperature in Celsius: "))
farenheit = 32+celsius*(9/5)
round_farenheit = round(farenheit, 2)
print(f"Its {round_farenheit} Farenheit")