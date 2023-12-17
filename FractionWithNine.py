
# Online Python - IDE, Editor, Compiler, Interpreter
import decimal

#def to find how many decimal digits are in a given number
def find_decimals(value):
    return (abs(decimal.Decimal(str(value)).as_tuple().exponent)) 

#input a non reapeating part of a recurring number and then a reapeating part
NoRepeat = float(input("Write the non repeating part of a recurring number: "))
Repeat = input("Write the repeating part of a recurring number: ")

if (NoRepeat.is_integer()):
    NoRepeat = int(NoRepeat)
    print("You wrote the number " + str(NoRepeat) + str(".") + Repeat + " and number " + Repeat + " is repeated.") 
else:
    print("You wrote the number " + str(NoRepeat) + Repeat + ", and number " + Repeat + " is repeated.") 

#number of decimal digits of non repeating part of the number is put in 2 different variables
NumberBehindDot1 = find_decimals(NoRepeat)
NumberBehindDot2 = find_decimals(NoRepeat)

#check how many decimal digits are there and for every decimal digit multiply {i} by 10
i = 1
if (NumberBehindDot1>0):
    while True:
        NumberBehindDot1 -= 1
        i *= 10
        if NumberBehindDot1 == 0:
            break

#get a part of the number that doesn't repeat as a whole number with all digits
NoRepeatNew = int(NoRepeat * i)

#get a part of the number that doesn't repeat and part of the number that repeats and put it together as a whole number with all digits
WholeNumber = str(NoRepeatNew) + str(Repeat)

#checks how many digits are repeated and for every digit add 1 to {j}
j = 0
while True:
    j += 1
    Repeat = int(Repeat) //10
    if Repeat == 0:
        break

#adds nines based on the number of digits under the period
nine = str("")
while (j>0):
    j -= 1
    nine += str("9")

#adds zeros based on the number of digits behind the dot
null = str("")
while (NumberBehindDot2>0):
    NumberBehindDot2 -=1
    null += str("0")

#the dedominator in the fraction
v = str(nine) + str(null)

#print formula how to calculate a recurring number into a fraction with nine
Formula = ("" + (str(int(WholeNumber)-int(NoRepeatNew)) + "/" + str(v)))
print(Formula)
