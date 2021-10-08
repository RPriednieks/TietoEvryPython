# Exercise 1a and 2a
# Example for input: 22.3, 23.2, 44.5, 46.9, 55.7, 122.4, 66.9

# entered_numbers = input("Enter several numbers (comma separated):")
# if entered_numbers == "q":
#     print("You decided to quit")
# else:
#     numbers_list = entered_numbers.split(", ")
#     summa = 0
#     for i in numbers_list:
#         summa += float(i)
#
#     average = summa / len(numbers_list)
#     saraksts = ", ".join(numbers_list)
#     print(f"You did enter these numbers: {saraksts} and average of those is: {average}")
#     print(numbers_list.sort())

# Exercise 3a
# Example for input: 22.3, 23.2, 44.5, 46.9, 55.7, 122.4, 66.9

entered_numbers = input("Enter several numbers (comma separated): ")
if entered_numbers == "q":
    print("You decided to quit")
else:
    numbers_list = entered_numbers.split(", ")
    new_numbers_list = []
    for i in numbers_list:
        new_numbers_list.append(float(i))

    new_numbers_list.sort()
    average = (new_numbers_list[-1] + new_numbers_list[-2] + new_numbers_list[-3] + new_numbers_list[0] + new_numbers_list[1] + new_numbers_list[2]) / 6
    print(
    f'''
TOP3 numbers are: {new_numbers_list[-1]}, {new_numbers_list[-2]} , {new_numbers_list[-3]}
BOTTOM3 numbers are: {new_numbers_list[0]}, {new_numbers_list[1]} , {new_numbers_list[2]}
Average of these numbers are: {average}
    ''')




