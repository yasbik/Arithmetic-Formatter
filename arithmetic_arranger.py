import string


def arithmetic_arranger(problems):

    arranged_problems = ["", "", ""]

    # there can only be a maximum of five problems
    # anything more will throw an error
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    
    num1_list = list()
    num2_list = list()
    dash_list = list()
    
    # loop through all the individual problems
    for calculation in problems:

        # separate each number and operand
        parts = calculation.split(" ")
        num1 = parts[0].strip()
        opperand = parts[1].strip()
        num2 = parts[2].strip()

        print(opperand)

        # opperand has to be an addition or a subtraction
        # anything else will throw an error and break the loop
        if not (opperand == '+' or opperand == '-'):  
            arranged_problems = "Error: Operator must be '+' or '-'."
            break

        # check that the strings only contain numbers
        # anything else will throw an error and break the loop
        if not num1.isnumeric() or not num2.isnumeric():
            arranged_problems = "Error: Numbers must only contain digits."
            break

        # each number can only be four digits long
        # anything else will break the loop
        if len(num1) > 4 or len(num2) > 4:
            arranged_problems = "Error: Numbers must only contain digits."
            break

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
                temp -= 1
            num1_list.insert(0, " ")
            num1_list.insert(0, " ")
            num2_list.insert(0, opperand)
        else:
            len_diff = (len(num2_list) - len(num1_list)) + 2
            while len_diff > 0:
                num1_list.insert(0, " ")
                len_diff -= 1
            num2_list.insert(0, " ")
            num2_list.insert(0, opperand)
        
        while biglen > 0:
            dash_list.append("-")
            biglen -= 1
        
        arranged_problems[0] += ''.join(num1_list)
        arranged_problems[1] += ''.join(num2_list)
        arranged_problems[2] += ''.join(dash_list)
        
        # print("Calculation =", calculation)
        # print("Parts = ", parts)
        # print(string.format("%4d%4d", int(num1), num2))

        arranged_problems = ""            
    

    return arranged_problems


