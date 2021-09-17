# File name: hw1.py
# Created by: Yuxiao Wu
# Created on : 9/15/2021
# no collaborators, no late days
# source for formula: https://sciencenotes.org/surface-area-formulas-volume-formulas/


# Problem 6
# save the words in the sentence "Hi my name is Bob" into variables and print.
def write_sentence():
    sentence = "Hi my name is Bob"
    print(sentence)


# Problem 7
# take in two integers a and b and calculate the bitwise or result.
def bit_or(a, b):
    return a | b


# Problem 8
# input the number of hours since Wed, Jan 1st 2020 at 12am, return a string result
def calculate_day(num_hours):
    num_day = num_hours / 24  # number of days elapsed
    hour = num_hours % 24  # hours in the day
    day = num_day % 7  # days in the week
    if day == 0:
        day_str = "Wednesday "
    elif day == 1:
        day_str = "Thursday "
    elif day == 2:
        day_str = "Friday "
    elif day == 3:
        day_str = "Saturday "
    elif day == 4:
        day_str = "Sunday "
    elif day == 5:
        day_str = "Monday "
    else:
        day_str = "Tuesday "

    if hour < 12:
        hour_str = "at " + str(hour) + " AM"
    else:
        hour_str = "at " + str(hour - 12) + " PM"
    daytime = day_str + hour_str
    return daytime


# Problem 9
# calculates the volume of sphere or cone with input radius and height
def calculate_volume(shape, dimensions):
    if shape == "sphere":
        volume = round(4 / 3 * 3.14 * dimensions ** 3, 2)
        return volume
    elif shape == "cone":
        volume = round(1 / 3 * 3.14 * dimensions[1] * dimensions[0] ** 2, 2)
        return volume
    return "Invalid Shape"

# end
a = calculate_volume("con", (3,7))
print(a)

