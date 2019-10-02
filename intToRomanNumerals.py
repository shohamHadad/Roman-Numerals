"""
class: convert a int number to Roman numeral
"""

class intToRomanNumerals():

    """
    constructor
    """
    def __init__(self, number):
        self.number = int(number)



    def intToRoman(self):
        """
            function name:intToRoman
            operation:The function get number and convert the number to Roman numerals
            :return: The function return string of Roman numerals
            """
        DecimalsMap = [1000000,900000,500000,400000,100000,90000,50000,40000,10000,9000,5000,4000,1000,900,500,400,100,90,50,40,10,9,5,4,1]
        RomanNumeralsMap= ['M','CM','D','CD','C','XC','L','XL','X','IX','V','MV','M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        arr = ['_','__','_','__','_','__','_','__','_','__','_',' _','','','','','','','','','','','','','']
        temp = self.number
        romanNum = ''
        bigNumber = ''
        i = 0
        while(self.number>0):
            #I am checking if I can subtract the large number in the dictionary
            # that I have for representing Roman numerals
            if ((self.number - DecimalsMap[i])>=0):
                # If the result is greater than zero it means
                # that I need to add the representation to the number
                romanNum = romanNum + RomanNumeralsMap[i]
                self.number = self.number - DecimalsMap[i]
            else:
                i = i +1

        i = 0
        #For numbers larger than 4000 there is a special representation with a line above Roman numerals
        #I keep the representation of the line up to know how to display it when I convert to the Roman number
        while(temp >0):
            if ((temp - DecimalsMap[i]) >= 0):
                bigNumber = bigNumber + arr[i]
                temp = temp - DecimalsMap[i]
            else:
                i = i+1

        #return string of Roman numerals
        return romanNum, bigNumber
