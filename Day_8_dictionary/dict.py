# Exercise 1


def get_char_count(text):
    blank_dict = {}
    for i in text():
        if i in blank_dict:
            blank_dict[i] += 1
        else:
            blank_dict[i] = 1
    return blank_dict


print(get_char_count("janis Janis"))

# Exercise 2


def replace_dict_value (d, bad_val, good_val):
    for k in d:
        if d[k] == bad_val:
            d[k] = good_val
    return d


d = {'a': 5, 'b': 6, 'c': 5}
print(replace_dict_value(d, 5, 10))

# Exercise 3a


def clean_dict_value (d, bad_val):
    new_dict = {key: value for key, value in d.items() if value != bad_val}
    return new_dict


d = {'a': 5, 'b': 6, 'c': 5}
print(clean_dict_value(d, 5))

# Exercise 3b


def clean_dict_values (d, v_list):
    new_dict = {key: value for key, value in d.items() if value not in v_list}
    return new_dict


d = {'a': 5, 'b': 6, 'c': 5, 'd':3}
l = [3,4,5]
print(clean_dict_values (d, l))