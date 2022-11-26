import string


def arithmetic_arranger(problems, solved = False):

    arranged_problems = ""

    # there can only be a maximum of five problems
    # anything more will throw an error
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems 

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    
    # loop through all the individual problems
    for calculation in problems:

        num1_list = list()
        num2_list = list()
        dash_list = list()
        result = 0

        # separate each number and operand
        parts = calculation.split(" ")
        num1 = parts[0].strip()
        opperand = parts[1].strip()
        num2 = parts[2].strip()

        # check that the strings only contain numbers
        # anything else will throw an error
        if not num1.isnumeric() or not num2.isnumeric():
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems

        # if the operator is an addition or subtraction, do the calculation
        # anything else will throw an error
        if opperand == "+":
            result = int(num1) + int(num2)
        elif opperand == "-":
            result = int(num1) - int(num2)
        else:
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
        
        # each number can only be four digits long
        # anything else will throw an error
        if len(num1) > 4 or len(num2) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems

        # add each individual digit of the first number into its list
        counter = 0
        while counter < len(num1):
            num1_list.append(num1[counter])
            counter += 1
        
        # add each individual digit of the second number into its list
        counter = 0
        while counter < len(num2):
            num2_list.append(num2[counter])
            counter += 1
        
        # keep track of the longest number and its length
        # the first number is assumed to be longer by default
        bignum = num1_list
        biglen = len(num1_list) + 2

        # if the second number is longer, update bignum and biglen
        if len(num2_list) > len(num1_list):
            bignum = num2_list
            biglen = len(num2_list) + 2
        
        # if the first number was longer,
        # find the difference in length it has with the second number
        if bignum == num1_list:
            len_diff = (len(num1_list) - len(num2_list)) + 1

            # add spaces to fill up the length difference
            while len_diff > 0:
                num2_list.insert(0, " ")
                len_diff -= 1
            
            # add spaces in front of the first number
            num1_list.insert(0, " ")
            num1_list.insert(0, " ")

            # add the operand in front of the second number
            num2_list.insert(0, opperand)

        # if the second number was longer,
        # find the difference in length it has with the first number
        else:
            len_diff = (len(num2_list) - len(num1_list)) + 2

            # add spaces to fill up the length difference
            while len_diff > 0:
                num1_list.insert(0, " ")
                len_diff -= 1
            
            # add the operator and a space in front of the second number
            num2_list.insert(0, " ")
            num2_list.insert(0, opperand)

        # add the result to the last line, while maintaining right justification
        line4 += str(result).rjust(biglen)

        # draw the dashes based on the length of the longer number     
        while biglen > 0:
            dash_list.append("-")
            biglen -= 1
        
        # add the list to the first three lines
        line1 += ''.join(num1_list)
        line2 += ''.join(num2_list)
        line3 += ''.join(dash_list)

        # add spaces after each problem
        if calculation != problems[-1]:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "

    # if the second parameter is true, then display the result 
    if solved:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    # otherwise just format the problems
    else:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3

    return arranged_problems



