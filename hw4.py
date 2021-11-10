# File name: hw4.py
# Created by: Yuxiao Wu
# Created on : 10/16/2021
# no collaborators, no late days
# source: textbook, Slides

# Problem 4
# Implement a Doubly-linked List

# Node class
class Node:

    # Initialize the node with variable value, prev and next
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    # returns the prev node
    def get_prev(self):
        return self.prev

    # returns the next node
    def get_next(self):
        return self.next

    # returns the value of the node
    def get_value(self):
        return self.value

    # set the previous node
    def set_prev(self, node):
        self.prev = node

    # set the next node
    def set_next(self, node):
        self.next = node

    # set the value of the node
    def set_value(self, val):
        self.value = val


# DoublyLinkedList Class
class DoublyLinkedList:

    # Initialize the DoublyLinkedList
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_to_end(self, val):
        # if list is empty, set the head
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head

        else:
            self.tail.next = Node(val, self.tail)
            self.tail = self.tail.next
        self.count += 1

    def add_to_front(self, val):
        # if list is empty, set the head
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head

        else:
            self.head.prev = Node(val, None, self.head)
            self.head = self.head.prev
        self.count += 1

    def delete(self, val):
        start = self.head
        for _ in range(self.count):
            if start.get_value() == val:
                # condition if deleting first element
                if start.prev is None:
                    start.next.prev = None
                    self.head = start.next
                    self.count -= 1
                    return
                # condition if deleting last element
                elif start.next is None:
                    start.prev.next = None
                    self.tail = start.prev
                    self.count -= 1
                    return
                # common situation
                else:
                    start.prev.next = start.next
                    start.next.prev = start.prev
                    self.count -= 1
                    return
            start = start.next

    def reverse(self):
        # if list is empty or only one element, do nothing
        if self.count <= 1:
            return
        else:
            start = self.head
            # Swap the prev and next for each node
            for _ in range(self.count):
                temp = start.prev
                start.prev = start.next
                start.next = temp
                start = start.prev
            # Swap the head and tail of the list
            temp = self.head
            self.head = self.tail
            self.tail = temp

    def compare(self, lst):
        start = self.head
        if len(lst) != self.count:
            return False
        for i in range(self.count):
            if start.get_value() != lst[i]:
                return False
            start = start.next
        return True

    def find(self, val):
        start = self.head
        index = 0
        for _ in range(self.count):
            if start.get_value() == val:
                return index
            start = start.next
            index += 1

    def __str__(self):
        list = []
        start = self.head
        for i in range(self.count):
            list.append(start.get_value())
            start = start.next
        return str(list)


# Problem 5
# implement the merge sort algorithm
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        # Sort the two halves
        merge_sort(left)
        merge_sort(right)
        b = c = d = 0
        while b < len(left) and c < len(right):
            if left[b] < right[c]:
                lst[d] = left[b]
                b += 1
            else:
                lst[d] = right[c]
                c += 1
            d += 1
        while b < len(left):
            lst[d] = left[b]
            b += 1
            d += 1
        while c < len(right):
            lst[d] = right[c]
            c += 1
            d += 1
    return lst


# Problem 6
# List to dictionary
def lst_to_dict(lst, start, end):
    """
    function lst_to_dict return a dictionary with all integers between the
    start and end number (inclusive) as the keys and their respective indices in the list as the value.
    :param lst: a list of unsorted numbers
    :param start: a start number
    :param end: a end number
    """
    result_dict = dict()
    index_dict = dict()
    for i in range(len(lst)):
        index_dict.update({lst[i]: i})
    lst.sort()
    start_end = range(start, end + 1)
    j = 0
    for ele in lst:
        while ele > start_end[j] and j < len(start_end) - 1:
            j += 1
        if ele == start_end[j]:
            result_dict.update({ele: index_dict.get(ele)})
    for i in range(start, end + 1):
        if result_dict.get(i) is None:
            result_dict.update({i: None})

    return result_dict


# Problem 7
# Target sum function
def target_sum(lst, target):
    """
    function target_sum takes a given list and returns the indices of two numbers that add up to a
    specific number.
    :param lst: the input lst
    :param target: the target sum
    """
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] + lst[j] == target:
                return i, j
    return

