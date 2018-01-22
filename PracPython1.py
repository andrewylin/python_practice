#!/usr/bin/env python

def solution():
    name = raw_input("What is your name?: ")
    age = raw_input("What is your age?: ")
    number = raw_input("Give me a number: ")

    try:
        age = int(age)
        number = int(number)
    except ValueError:
        print "one of the numbers you gave was not a number... :("
        return
    try:
        assert age >= 0
    except:
        print "you cannot be negative age :("
        return

    yearsTo100 = 100 - age
    print number*("Hello " + name + "! You will be 100 in the year " + \
            str(yearsTo100 + 2018) + "\n")

solution()
