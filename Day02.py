"""
Day 2 Advent of Code
Make a counter for RockPaperScissors.
1 = Rock = A (or = X)
2 = Paper = B (or = Y)
3 = Scissors = C (or = Z)

X = Loss
Y = Draw
Z = Win

Lost = 0
Draw = 3
Win = 6

Paper beats rock
Rock beats scissors
Scissors beat paper
"""
choice = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9, 
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}
results = {
    "A X": 3, 
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9, 
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}
with open("Day02-input.txt",'r') as data_file:
    score = sum([results[item] for item in data_file.read().split("\n")])
    print(score)