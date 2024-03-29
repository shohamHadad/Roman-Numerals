# Roman-Numerals
Roman numeral calculator


**Python program Roman numerals converter:** 
* Decimal to Roman
* Roman to Decimal

**Installation:** 
- Install Python 3

**Usage:**
- cd  /program-folder
- python3 main.py


Decimal to Roman
===============
General structure: 
1. User input : Decimal number
2. Input validation:
	- Valid decimal check 
	- Decimal inserted is in the Roman numerals range: [ 1 - 3,999,999 ]
3. Conversion done using a pre-defined Roman numerals map (see convertion code provided below) 


**Conversion code:**
Input: inputNumber
decimalsMap = [1000,900,500,400,100…….]
romanNumeralsMap = [M,CM,D,CD,C…..]
result = “”
Ii = 0
while(inputNumber>0):
	if (inputNumber - DecimalsMap [i] >=0):
		result +=  RomanNumeralsMap [i]
		inputNumber -= DecimalsMap[i]
	else:
i +=1
return result


**Remarks:**
Large numbers are represented with line above the number. 
An upper line above a numeral or Roman number symbolizes multiplying by 1,000 for example:

![תמונה להערות](https://user-images.githubusercontent.com/33810472/66054042-1420c080-e53c-11e9-89a4-2aeeee4f4040.png)


So to calculate a number greater than 3,999 that can be represented as a regular without a top line, I added an array that contains only the representation of the top line for all numbers

Therefore if the user enters a number greater than 3,999 when the result is printed, the number will be printed with the top line accordingly
for example:

![input and output](https://user-images.githubusercontent.com/33810472/66060340-2869bb00-e546-11e9-83b3-fdab871d35a0.png)



Roman to Decimal
===============
**General structure:** 
1. User input : Roman chars
2. Input validation:
	- Non decimal, Roman characters validity 
	- In addition, substring validity: for example, such a sub string "VV" may not represent Roman numerals
3. Conversion done using a pre-defined Roman numerals dictionary (see conversion code provided below) 


Input: romanInput
romanNumeralsDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
result = 0
For i in range(0,len(romanInput)):
	If i+1 < len(romanInput):
		If romanNumeralsDict[romanInput[i+1]] > romanNumeralsDict[romanInput[1]]:
			result  -= romanNumeralsDict[romanInput[1]]
else:	
result  += romanNumeralsDict[romanInput[1]]	
	else:
		result  += romanNumeralsDict[romanInput[1]]

return result 

![input and output example 2](https://user-images.githubusercontent.com/33810472/66060821-f60c8d80-e546-11e9-879a-9c4b9d9ef9a3.png)

