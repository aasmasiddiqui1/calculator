#create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. 
#Your Program should format  the output in a readable manner

#Get input from user
num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
operations = input("Enter operation(+,-,*,/,**,//,%): ")

#perform the requested operation
if operations == "+":
    result  = num1 + num2
elif operations == "-":
    result = num1 - num2
elif operations == "*":
    result = num1 * num2
elif operations == "/":
    result = num1 / num2
elif operations == "**":
    result = num1 ** num2
elif operations == "//":
    result = num1 // num2
elif operations == "%":
    result = num1 % num2
else:
    #if the operation is not valid
    print("Invalid Operator")

#Print the result in a formatted manner
print("{} {} {} = {}".format(num1,operations, num2, result))