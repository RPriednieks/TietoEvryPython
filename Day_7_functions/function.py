# Exercise 1

def add_mult():
    my_nums = [int(t) for t in input("Enter three values separated by whitespace: ").split(" ")]
    my_nums.sort()
    result = (my_nums[0]+my_nums[1]) * my_nums[2]
    print(result)

add_mult()

# Exercise 2

def is_palindrome():
    text = input("Enter some text: ").lower()
    normal_list = text.split()
    print(normal_list)
    reverse_list = [i[::-1] for i in normal_list]
    reverse_list.reverse()
    if normal_list == reverse_list:
        print("This is palindrome")
    else:
        print("This is not palindrome")
    print(reverse_list)

is_palindrome()




#input