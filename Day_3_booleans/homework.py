#Exercise 1

temperature = int(input("What's your temperature?"))
if temperature < 35:
    print("not too cold")
elif 35 <= temperature <= 37:
    print("all right")
else:
    print("possible fever")

#Exercise 2

salary = int(input("What is your monthly salary?"))
years = float(input("How may years have you worked for company?"))
if years > 2:
    bonus = (years - 2) * ((15 * salary) / 100.0)
    print(f"Your bonus is {bonus} euro")
else:
    print("You do not qualify for bonus!")

#Exercise 3

number1 = float(input("Enter random number: "))
number2 = float(input("Enter random number: "))
number3 = int(input("Enter random number: "))

first = 0
second = 0
third = 0

if number1 < number2 and number1 < number3:
    first = number1
    if number2 < number3:
        second = number2
        third = number3
    else:
        second = number3
        third = number2

if number1 > number2 and number1 < number3:
    second = number1
    if number2 < number3:
        first = number2
        third = number3
    else:
        first = number3
        third = number2

if number1 > number2 and number1 > number3:
    third = number1
    if number2 < number3:
        first = number2
        second = number3
    else:
        first = number3
        second = number2

print(f"Ascending order is {first}, {second}, {third}")