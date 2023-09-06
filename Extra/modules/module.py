#!/usr/bin/enc python3

"""this is a module for demonstrating how to use and write modules"""


__counter = 0


def sum1(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prod1(the_list):
    global __counter
    __counter += 1
    the_prod = 1
    for element in the_list:
        the_prod *= element
    return the_prod


if __name__ == '__main__':
    print('This program is being run by itself. I prefer to be a module some day')
    my_list = [i+1 for i in range(5)]  # list comprehension to create a list
    print(sum1(my_list) == 15)
    print(prod1(my_list) == 120)
