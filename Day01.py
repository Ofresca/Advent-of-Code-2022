"""
Code for the first day of Advent of Code. 
Count calories and number of items in a list, seperated by " "
"""


with open("Day01-input.txt",'r') as data_file:
    listlist = [item.split("\n") for item in data_file.read().split("\n\n")]
    sumlistlist = sum(sorted([sum([int(item) for item in clist]) for clist in listlist])[-3:])
    print(sumlistlist)








