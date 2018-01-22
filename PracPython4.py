#!/usr/bin/env python

def solution(number):
    list = []
    for i in range(1, number):
        if number % i == 0:
            list.append(i)
    print "Divisors:"
    print list

a = raw_input("Plese input a number: ")
try:
    a = int(a)
except ValueError:
    print "You didn't input a number. :("
    exit()
solution(a)
