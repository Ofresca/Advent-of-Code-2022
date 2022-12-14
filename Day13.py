input = open("Day13-input.txt",'r').read().split('\n\n')
import ast

# def compare2(list1, list2, rule):
#     if isinstance(list1, int) and isinstance(list2,int):
#         if list1 < list2:
#                 #Line is in correct order
#             correct.append(rule)
#             print('3 correct', correct, rule)
#             return True
#         elif list1 > list2:
#             #Line is in incorrect order
#             incorrect.append(rule)
#             print('4 incorrect', incorrect, rule)
#             return True
#         elif list1 == list2:
#             """do nothing and continue checking"""
            
#     elif not isinstance(list1, int) and not isinstance(list2,int):
#         l1, l2 = len(list1), len(list2)
#         l3 = min(l1,l2)
#         for i in range(l3):
#             z = compare2(list1[i], list2[i], rule)
#             if z: 
#                 return True
#         if l1 > l2:
#             incorrect.append(rule)
#             return True
#         elif l1 < l2:
#             correct.append(rule)
#             return True

#     elif not isinstance(list1,int):
#         if list1 == []:
#             correct.append(rule)
#             return True
#         else: 
#             z = compare2(list1[0], list2, rule)
#             if z: 
#                 return True
#             else:
#                 incorrect.append(rule)
#                 return True

#     elif not isinstance(list2,int):
#         if list2 == []:
#             incorrect.append(rule)
#             return True
#         z = compare2(list1, list2[0], rule)
#         if z: 
#             return True
#         else:
#             correct.append(rule)
#             return True

def compare2(list1, list2):
    if isinstance(list1, int) and isinstance(list2,int):
        if list1 < list2:
            return 1
        elif list1 > list2:
            return -1
        elif list1 == list2:
            return 0
            
    elif not isinstance(list1, int) and not isinstance(list2,int):
        l1, l2 = len(list1), len(list2)
        l3 = min(l1,l2)
        for i in range(l3):
            z = compare2(list1[i], list2[i])
            if z != 0: 
                return z
        if l1 > l2:
            return -1
        elif l1 < l2:
            return 1
        else:
            return 0

    elif not isinstance(list1,int):
        if list1 == []:
            return 1
        return compare2(list1[0], list2)

    elif not isinstance(list2,int):
        if list2 == []:
            return -1
        return compare2(list1, list2[0])

rule = 0
correct = []
incorrect = []

for line in input:
    rule += 1
    left, right = line.split('\n')
    left, right = ast.literal_eval(left), ast.literal_eval(right)
    
    compare2(left, right, rule)

print('End correct', correct)
print('ans', sum(set(correct))) 

# # Part 2 ------------------------------------------------------------

# def sorts(list1, list2, rule):
#     # print('1', 'list1:', list1, 'list2:', list2)
#     if isinstance(list1, int) and isinstance(list2,int):
#         if list1 < list2:
#                 #Line is in correct order
#             swapped.append(False)
#             # print(1)
#             return True
#         elif list1 > list2:
#             #Line is in incorrect order
#             swapped.append(True)
#             # print(2)
#             return True
#         elif list1 == list2:
#             """do nothing and continue checking"""
#             # print(3)
#             return None
            
#     elif not isinstance(list1, int) and not isinstance(list2,int):
#         l1, l2 = len(list1), len(list2)
#         l3 = min(l1,l2)
#         for i in range(l3):
#             z = sorts(list1[i], list2[i], rule)
#             if z: 
#                 # print(4)
#                 return True
#         if l1 > l2:
#             swapped.append(True)
#             # print(5)
#             return True
#         elif l1 < l2:
#             swapped.append(False)
#             # print(6)
#             return True

#     elif not isinstance(list1,int):
#         if list1 == []:
#             swapped.append(False)
#             # print(7)
#             return True
#         else: 
#             z = sorts(list1[0], list2, rule)
#             if z: 
#                 # print(8)
#                 return True
#             else:

#                 # swapped.append(True)
#                 # print(9)
#                 return None
#                 # return True

#     elif not isinstance(list2,int):
#         if list2 == []:
#             swapped.append(True)
#             # print(10)
#             return True
#         z = sorts(list1, list2[0], rule)
#         if z: 
#             # print(11)
#             return True
#         else:
#             # swapped.append(False)
#             # print(12)
#             return None
#             # return True


rule = 0

lines = [ast.literal_eval(text) for line in input for text in line.split('\n')]

lines.append([[2]])
lines.append([[6]])

n = len(lines)
swapped = []

print(lines)

for i in range(n-1):
    for j in range(0,n-i-1):
        sorts(lines[j], lines[j+1], rule)
        # print(swapped[-1])
        if swapped[-1] == True:
            lines[j], lines[j+1] = lines[j+1], lines[j]

print(lines)
d2 = [i+1 for i in range(len(lines)) if lines[i] == [[2]]]
d6 = [i+1 for i in range(len(lines)) if lines[i] == [[6]]]

print('d2', d2, 'd6', d6)
print(int(d2[0])*int(d6[0]))