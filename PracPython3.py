#!/usr/bin/env python

def solution(list):
    number = raw_input("GIVE ME A NUMBER FOOL: ")
    try:
        number = int(number)
    except ValueError:
        print "YOU DIDN'T GIVE ME A NUMBER FOOL!"
        return

    count = 0
    newlist = []
    for item in list:
        if item < number:
           print item
           newlist.append(item)
    print newlist
    return

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
solution(a)
