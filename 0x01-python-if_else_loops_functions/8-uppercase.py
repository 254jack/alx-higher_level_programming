#!/usr/bin/python3
def uppercase(s):
    for char in s:
        a = ord(char)
        if 97 <= a <= 122:
            a -= 32 
            char = chr(a)
        print("{}".format(char), end="")
    print("")
