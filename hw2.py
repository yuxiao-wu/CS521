# File name: hw2.py
# Created by: Yuxiao Wu
# Created on : 9/28/2021
# no collaborators, no late days
# source: textbook

# Problem 5
# Take a float input grade and returns the letter string
def calculate_letter(score):
    if score >= 93:
        letter = "A"
    if 93 > score >= 90:
        letter = "A-"
    if 90 > score >= 87:
        letter = "B+"
    if 87 > score >= 83:
        letter = "B"
    if 83 > score >= 80:
        letter = "B-"
    if 80 > score >= 77:
        letter = "C+"
    if 77 > score >= 73:
        letter = "C"
    if 73 > score >= 70:
        letter = "C-"
    if 70 > score >= 50:
        letter = "D+"
    else:
        letter = "F"
    return letter


# Problem 6
# take an input year and check if it is a leap year by returning True or False
def is_leap(year):
    if year // 4 == 0 and year // 100 != 0 or year // 400 == 0:
        return True
    else:
        return False


print(is_leap(1000))
a = is_leap(1000)
