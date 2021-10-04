import string

# Exercise 1

name = input("Input your name: ")
extra = ",a thorough mess is it not "
print(name[::-1] + extra + name[0] + "?")

# Exercise 2

name = input("Player 1: Input two or more words: ")
for i in name:
    if i.isalpha():
        print("*", end="")
    else:
        print(" ", end="")

guess = input(f"\nPlayer 2: Guess a symbol: ")
low_guess = guess.lower()
for y in name:
    if y.lower() == low_guess:
        print(y, end="")
    elif y.isalpha():
        print("*", end="")
    else:
        print(" ", end="")

# Exercise 3