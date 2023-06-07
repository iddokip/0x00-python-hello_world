#!/bin/python3

# ask the user to input two values and store the vairable num1 and nu2
# convert the sting the users input into regular numbers
# add th variables and store into a variable sum
num2, num1 = input('enter 2 numbers').split()
num1 = int(num1)
num2 = int(num2)
sum = num1 + num2
quotient = num1 / num2
product = num1 * num2
remainder = num1 % num2
difference = num1 + num2
# print the result
print("{} + {} = {}".format(num1, num2, sum))
print("{} * {} = {}".format(num1, num2, product))
print("{} /  {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
print("{} - {} = {}".format(num1, num2, difference))
