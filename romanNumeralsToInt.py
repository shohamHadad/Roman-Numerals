"""
class: convert a Roman numeral to int number
"""

class romanNumeralsToInt():

    """
    constructor
    """
    def __init__(self, number):
        self.number = number


    def romanToInt(self):
        """
        function name:romanToInt
        operation:The function get string of Roman numerals and convert to int number
        :return: The function return int number
        """
        dictRomanNumerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        lenStringNum = len(self.number)
        integerNum = 0

        #In writing a number, the digits are written from left to right, from the largest to the smallest.
        # If a small number appears to the left of its larger number,subtract the smaller number from
        #the total number
        #I pass a character in a string and check
        # if this case happens and connects and subverts accordingly
        for i in range(0,lenStringNum):
            if i +1 < lenStringNum:
                if(dictRomanNumerals[self.number[i+1]] > dictRomanNumerals[self.number[i]]):
                    integerNum = integerNum - dictRomanNumerals[self.number[i]]
                else:
                    integerNum = integerNum + dictRomanNumerals[self.number[i]]
            else:
                integerNum = integerNum + dictRomanNumerals[self.number[i]]
        return integerNum

