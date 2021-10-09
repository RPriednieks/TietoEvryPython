# Exercise 1

aggr = []
while True:
    entered_numbers = input("Enter numbers and press Enter, or q to quit: ")
    if entered_numbers.lower() == "q":
        break
    else:
        aggr.append(float(entered_numbers))
        print(f"All numbers: {aggr}, Average is {sum(aggr) / len(aggr)}")
        print(f"TOP3 {sorted(aggr)[-3:]}")
        print(f"BOTTOM3 {sorted(aggr)[:3]}")

# Exercise 2

aggr = []
start = int(input("Enter first number: "))
last = int(input("Enter last number: "))

for i in range(start, last+1):
    cube = i**3
    print(f"{i} cubed: {cube}")
    aggr.append(cube)
print(f"All cubes: {aggr}")

# Exercise 3

sentence = input("Enter some text: ")
words = sentence.split()
reversed_word_list = [i[::-1] for i in words]
new_text = " ".join(reversed_word_list).capitalize()
print(f"{sentence} --> {new_text}")


# Exercise 4

question = int(input("Enter how many prime numbers would you like to see: "))
primes = []
num = 1
while len(primes) < question:
    num += 1
    not_prime = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                not_prime = True
                break
    if not_prime:
        continue
    primes.append(num)
print(primes)