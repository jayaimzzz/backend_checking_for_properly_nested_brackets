
import sys

def main(filename):
    file = open(filename, "r").readlines()
    my_list = []
    for line in file:
            result = check_line_for_nesting(line)
            print result

def check_line_for_nesting(line):
    line = split_line_into_list(line)
    dict1 = {
        "(": "paren",
        ")": "paren",
        "{": "curly",
        "}": "curly",
        "[": "square",
        "]": "square",
        "<": "greater_thank",
        ">": "greater_thank",
        "(*": "star",
        "*)": "star"
    }
    list1 = []
    for i, c in enumerate(line):
        if c in ["(","[","{","(*","<"]:
            list1.append(dict1[c])
        elif c in [")","]","}","*)",">"]:
            if dict1[c] == list1[-1]:
                list1.pop()
            else:
                return "No " + str(i + 1)
    if len(list1) == 0:
        return "Yes"
    else:
        return "No " + str(len(line) + 1)

# def check_line_for_nesting(line):
#     line = split_line_into_list(line)
#     curly_o = curly_c = paren_o = paren_c = square_o = square_c = star_o = star_c = greater_than = less_than = 0
#     for i, c in enumerate(line):
#         if c == "{":
#             curly_o += 1
#         if c == "(":
#             paren_o += 1
#         if c == "[":
#             square_o += 1
#         if c == "(*":
#             star_o += 1
#         if c == "<":
#             less_than += 1
#         if c == "}":
#             curly_c += 1
#         if c == ")":
#             paren_c += 1
#         if c == "]":
#             square_c += 1
#         if c == "*)":
#             star_c += 1
#         if c == ">":
#             greater_than += 1
        
#         if curly_c > curly_o or square_c > square_o or paren_c > paren_o or star_c > star_o or greater_than > less_than:
#             return "No " + str(i + 1)
#     if curly_c == curly_o and paren_c == paren_o and square_c == square_o and star_o == star_c and greater_than == less_than:
#         return "Yes"
#     else:
#         return "No " + str(len(line) + 1)

def split_line_into_list(line):
    list1 = list(line)[:-1]
    i = 0
    list2 = []
    length = len(list1)
    while i < length:
        if list1[i] == "(" and i < length - 1 and list1[i+1] == "*":
            list2.append("(*")
            i += 1
        elif list1[i] == "*" and i < length - 1 and list1[i+1] == ")":
            list2.append("*)")
            i += 1
        else:
            list2.append(list1[i])
        i += 1
    return list2

if __name__ == '__main__':
    """checks fro properly nested brackets"""
    filename = sys.argv[1]
    main(filename)