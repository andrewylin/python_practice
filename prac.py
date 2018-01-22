#!/usr/bin/env python

import helper
import sys

def ValidStack(stack):
    try:
        a = stack.pop()
    except:
        return False
    return a

def solution(string):
    stack = []
    for item in string:
        if item == "{" or item == "[" or item == "(":
            stack.append(item)
        elif item == "}":
            a = ValidStack(stack)
            if a != "{":
                return False
        elif item == "]":
            a = ValidStack(stack)
            if a != "[":
                return False
        elif item == ")":
            a = ValidStack(stack)
            if a != "(":
                return False
    if len(stack) != 0:
        return False
    return True

print solution("()")
print solution("())")
print solution("")
print solution("(")
print solution(")")
print solution("([({})])")
print solution("([({}))")
print solution("({})])")
