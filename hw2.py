# File name: hw2.py
# Created by: Yuxiao Wu
# Created on : 9/28/2021
# no collaborators, no late days
# source: textbook

import random


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
    if score < 50:
        letter = "F"
    return letter


# Problem 6
# take an input year and check if it is a leap year by returning True or False
def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


# Problem 7
# input a number and check if it is a triangular number by return True or False
def is_triangle(num):
    sum = 0
    for i in range(1, num):
        sum += i
        if sum == num:
            return True
            break

    return False


# Problem 8
# Find sum of all triangular numbers in an input range
def triangle_sum(lower_bound, upper_bound):
    sum = 0
    i = lower_bound
    while i <= upper_bound:
        if is_triangle(i):
            sum += i
        i += 1
    return sum


# Problem 9
# return a list of random digits(1-9) of input length n
def random_gen(n):
    list_rnd = []
    for _ in range(n):
        list_rnd.append(random.randint(1, 9))
    return list_rnd


# Problem 10
# Add each digit for an input number recursively until only one digit left
def digit_sum(num):
    num_left = num
    sum = 0
    while num_left >= 10:
        digit = num_left % 10
        sum += digit
        num_left //= 10
    sum += num_left
    if sum >= 10:
        sum = digit_sum(sum)
    return sum


print(calculate_letter(100))