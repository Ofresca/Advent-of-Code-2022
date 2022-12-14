"""
Advent of Code Day 03
"""

import string

rugsack = open("Day03-input.txt",'r').read().split("\n")

rugsack_total = sum([string.ascii_letters.index(char)+1 for list in rugsack for char in \
    set(list[0:len(list)//2]) & set(list[len(list)//2:])])

print(rugsack_total)

badge_total = sum([string.ascii_letters.index(char)+1 for i in range(0,len(rugsack),3) for char in \
    set(rugsack[i]) & set(rugsack[i+1]) & set(rugsack[i+2])])

print(badge_total)







