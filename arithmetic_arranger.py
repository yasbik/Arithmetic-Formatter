import string


def arithmetic_arranger(problems):

    arranged_problems = ""

    #print("\n", type(arranged_problems[0]))

    # there can only be a maximum of five problems
    # anything more will throw an error
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems 

    line1 = ""
    line2 = ""
    line3 = ""
    
    # loop through all the individual problems
    for calculation in problems:

        num1_list = list()
        num2_list = list()
        dash_list = list()

        # separate each number and operand
        parts = calculation.split(" ")
        num1 = parts[0].strip()
        opperand = parts[1].strip()
        num2 = parts[2].strip()

        # opperand has to be an addition or a subtraction
        # anything else will throw an error and break the loop
        if not (opperand == '+' or opperand == '-'):  
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems

        # check that the strings only contain numbers
        # anything else will throw an error and break the loop
        if not num1.isnumeric() or not num2.isnumeric():
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems

        # each number can only be four digits long
        # anything else will break the loop
        if len(num1) > 4 or len(num2) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems

        counter = 0
        while counter < len(num1):
            num1_list.append(num1[counter])
            counter += 1
        
        counter = 0
        while counter < len(num2):
            num2_list.append(num2[counter])
            counter += 1
        
        bignum = num1_list
        biglen = len(num1_list) + 2

        if len(num2_list) > len(num1_list):
            bignum = num2_list
            biglen = len(num2_list) + 2
        
        if bignum == num1_list:
            len_diff = (len(num1_list) - len(num2_list)) + 1
            while len_diff > 0:
                num2_list.insert(0, " ")
                len_diff -= 1
            num1_list.insert(0, " ")
            num1_list.insert(0, " ")
            num2_list.insert(0, opperand)
            # num1_list.append("\n")
            # num2_list.append("\n")
        else:
            len_diff = (len(num2_list) - len(num1_list)) + 2
            while len_diff > 0:
                num1_list.insert(0, " ")
                len_diff -= 1
            num2_list.insert(0, " ")
            num2_list.insert(0, opperand)
            # num1_list.append("\n")
            # num2_list.append("\n")
                
        while biglen > 0:
            dash_list.append("-")
            biglen -= 1
        
        line1 += ''.join(num1_list)
        line2 += ''.join(num2_list)
        line3 += ''.join(dash_list)

        if calculation != problems[-1]:
            line1 += "    "
            line2 += "    "
            line3 += "    "

        # print(arranged_problems[0])
        # print(arranged_problems[1])
        # print(arranged_problems[2])

        # arranged_problems[0] += "\n"
        # arranged_problems[1] += "\n"
        # arranged_problems[2] += "\n"
        
        # print("Calculation =", calculation)
        # print("Parts = ", parts)
        # print(string.format("%4d%4d", int(num1), num2))           
    
    arranged_problems = line1 + "\n" + line2 + "\n" + line3

    return arranged_problems



