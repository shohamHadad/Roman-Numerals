
from intToRomanNumerals import *
from romanNumeralsToInt import *


def main():
    stop = True
    #As long as the user has write exit, the program will print the game menu
    while(stop):
        printMenu()
        chosen = input()

        #This case when the user wants to convert a int number to Roman numeral
        if chosen == '1':
            num = 1
            check = True
            #checking the user's input
            while (check):
                print("Please insert a decimal number:")
                num = input()
                check = checkInput(num)
            roman = intToRomanNumerals(num)
            result = roman.intToRoman()
            if len(result[1])>0:
                print("The Roman format is:")
                print(result[1])
                print(result[0]+ "\n")
            else:
                print("The Roman format is: " + result[0] + "\n")

        #This case when the user wants to convert a Roman numeral to int number
        elif chosen == '2':
            num = 'I'
            check = True
            #checking the user's input
            while (check):
                print("Please insert a roman number:")
                num = input()
                check = checkRomanInput(num)
            roman = romanNumeralsToInt(num)
            result = roman.romanToInt()
            if result > 3999999 and result < 1:
                print("Please enter a valid Roman numeral or number from 1 to 3,999,999")
            else:

                print("The Number is: "+ str(result))
                print("\n")
        # Exit the program
        elif chosen == 'exit' or chosen == 'EXIT':
            stop = False
        else:
            print("Invalid input")

def printMenu():
    "This function print the game menu"
    print("Menu:")
    print("A:Choose 1 to convert from number to Roman numerals")
    print("B:Choose 2 to convert from Roman numerals to number ")
    print("C:For exit, write exit")

def checkInput(number):

    """
    function name:checkInput
    operation:The function get number and check if is valid in Roman numerals
    :parameter: number
    :return: The function return TRUE if the input is valid and FALSE if is invalid
    """

    #check if the user's input is number
    if (number.isdigit() == True):
        if int(number) < 1 or int(number) > 3999999:
            print("Invalid input")
            print("The minimal number to converter is:1")
            print("and the maximum number to converter is:3,999,999")
            print("Please enter a valid Roman numeral or number from 1 to 3,999,999")
            return True
        return False
    print("Invalid input")
    return True

def checkRomanInput(num):

    """
    function name:checkRomanInput
    operation:The function get string and check if is valid in Roman numerals
    :parameter: string Roman numerals
    :return: The function return TRUE if the input is valid and FALSE if is invalid
    """


    romanNumerals = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    if (num.isdigit() == True):
        print("Invalid input")
        print("Please enter only Roman numerals")
        return True
    else:
        lenNum = len(num)
        lenRomanNumerals = len(romanNumerals)
        for i in range(0,lenNum):
            check = False
            for j in range(0,lenRomanNumerals):
                if num[i] == romanNumerals[j]:
                    check = True
            if check == False:
                print("Invalid input")
                print("Please enter only Roman numerals")
                return True
    #Sub String that can't be in Roman numerals
    invalid = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM']
    if any(sub in num for sub in invalid):
        print("Invalid input")
        print("Please enter only Roman numerals")
        return True
    return False



if __name__ == '__main__':
    main()