#Exercise 1

virkne=""
for i in range(1, 101):
    if i % 5 == 0:
        virkne = virkne + "Fizz,"
    elif i % 7 == 0:
        virkne = virkne + "Buzz,"
    elif i % 5 == 0 and i % 7 == 0:
        virnkne = virkne + "FizzBuzz,"
    else:
        virkne = virkne + str(i) + ","
print(virkne)

#Exercise 2

height = input("Enter the height of the tree: ")
for i in range(1,int(height)+1):
    print((int(height) - i) * " " + ((i*2)-1) * "*")

#Exercise 3

prime = input("Enter any positive number: ")
if prime