
import sys

def main(filename):
    file = open(filename, "r").readlines()
    output_file = open (filename.split(".")[0] + "_output.txt","w")
    for line in file:
            result = check_line_for_nesting(line)
            output_file.write(result + "\n")
    output_file.close()
    
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
    """checks for properly nested brackets"""
    filename = sys.argv[1]
    main(filename)