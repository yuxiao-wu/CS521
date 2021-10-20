# File name: hw3.py
# Created by: Yuxiao Wu
# Created on : 10/16/2021
# no collaborators, no late days
# source: textbook

# Problem 3
# Take a list input and return a list where neighbors of each element are added to it
def neighbor_sum(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        result_list = [a_list[0] + a_list[1]]
        for i in range(1, len(a_list) - 1):
            result_list.append(a_list[i] + a_list[i - 1] + a_list[i + 1])
        result_list.append(a_list[len(a_list) - 1] + a_list[len(a_list) - 2])
    return result_list


# Problem 4
# Take a list of incomes and return the total income tax
def get_income_tax(list_of_incomes):
    for i in range(len(list_of_incomes)):
        list_of_incomes[i] = calculate_tax(list_of_incomes[i])
    return list_of_incomes


# Helper function to calculate the tax
def calculate_tax(income):
    if income <= 12550:
        income_tax = 0
    else:
        income -= 12550
        if income <= 9950:
            income_tax = 0.1 * income
        elif income <= 40525:
            income_tax = 0.1 * 9950 + 0.12 * (income - 9950)
        elif income <= 86375:
            income_tax = 0.1 * 9950 + 0.12 * (40525 - 9950) + 0.22 * (income - 40525)
        elif income <= 164925:
            income_tax = 0.1 * 9950 + 0.12 * (40525 - 9950) + 0.22 * (86375 - 40525) + 0.24 * (income - 86375)
        elif income <= 209425:
            income_tax = 0.1 * 9950 + 0.12 * (40525 - 9950) + 0.22 * (86375 - 40525) + 0.24 * (
                    164925 - 86375) + 0.32 * (income - 164925)
        elif income <= 523600:
            income_tax = 0.1 * 9950 + 0.12 * (40525 - 9950) + 0.22 * (86375 - 40525) + 0.24 * (
                    164925 - 86375) + 0.32 * (209425 - 164925) + 0.35 * (income - 209425)
        elif income > 523600:
            income_tax = 0.1 * 9950 + 0.12 * (40525 - 9950) + 0.22 * (86375 - 40525) + 0.24 * (
                    164925 - 86375) + 0.32 * (209425 - 164925) + 0.35 * (523600 - 209425) + 0.37 * (income - 523600)
    return income_tax


# Problem 5
# set operation class SetSuite
class SetSuite:

    # Part 1
    def __init__(self, list_of_lists):
        self.list_of_sets = []
        for ele in list_of_lists:
            if len(ele) > 0:
                set_list = set(ele)
                self.list_of_sets.append(list(set_list))

    # adds a new set to the internal list of sets
    def add_set(self, a_list):
        self.list_of_sets.append(list(set(a_list)))

    # returns the internal list of sets as a list
    def get_sets(self):
        return self.list_of_sets

    # returns a set that is the union of all sets in the class
    def union_all(self):
        union_set = []
        for ele in self.list_of_sets:
            union_set += ele
        return list(set(union_set))

    # returns a set that is the intersection of all setts in the class
    def intersection_all(self):
        intersection_set = set(self.list_of_sets[0])
        for i in range(len(self.list_of_sets) - 1):
            intersection_set = intersection_set.intersection(set(self.list_of_sets[i + 1]))
        return list(intersection_set)


# Problem 6
# Generate the i th row of pascal's triangle using recursion
def pascal(row):
    current_row = [1]
    if row == 0:
        return current_row
    prev_row = pascal(row - 1)
    for i in range(len(prev_row) - 1):
        current_row.append(prev_row[i] + prev_row[i + 1])
    return current_row + [1]


# Problem 7
# check if a number is a perfect power of another using recursion
def perfect_power(num_1, num_2):
    if num_2 == num_1 == 0 or num_2 == num_1 == 1:
        return True
    if (num_1 <= 1 and num_1 != num_2) or num_2 % num_1 != 0:
        return False
    else:
        if num_2 == num_1:
            return True
        else:
            num_2 = num_2 / num_1
            return perfect_power(num_1, num_2)


# Problem 8
# convert a given number and base to base 10
def convert_to_10(number, base):
    try:
        if base % 1 != 0:
            return "Invalid base"
        if len(number) <= 1:
            return int(number)
        else:
            digit = int(number[0])
            if digit >= base:
                return "Invalid Number"
            result = digit * pow(base, len(number) - 1)
        return result + convert_to_10(number[1:], base)
    except ValueError:
        print("Error: number Not a Number")
    except TypeError:
        print("Error: base Not a Number")


