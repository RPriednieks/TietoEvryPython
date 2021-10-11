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
    slick = "".join(normal_list)
    reverse_list = [i[::-1] for i in normal_list]
    reverse_list.reverse()
    slick2 = "".join(reverse_list)
    if slick == slick2:
        print("This is palindrome")
    else:
        print("This is not palindrome")

is_palindrome()

# Exercise 3

def get_city_year(p0, perc, delta, p):
    years = 0
    original_p0 = p0
    percentage_converted = float(perc/100)
    while p0 < p:
        if original_p0 > p0:
            years = -1
            break
        p0 = p0 + (p0 * percentage_converted) + delta
        years += 1
    print(years)

get_city_year(1000, 2, 50, 1200)
get_city_year (1000, 2, -50, 5000)
get_city_year (1500, 5, 100, 5000)
get_city_year (1500000, 2.5, 10000, 2000000)