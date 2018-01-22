#!/usr/bin/env python

def solution():
    number = raw_input("Please give me a number: ")
    try:
        number = int(number)
    except ValueError:
        print "YOU DIDN'T GIVE ME A NUMBER DOOFUS!"
        return

    if number%2 == 0:
        print "your number is even! yay!"
    else:
        print "why are you so odd"
    return

solution()
