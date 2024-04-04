num1 = float(input("Enter your value: "))
num2 = float(input("Enter your value: "))

opt = input("Enter your oprator: ")

if opt == "+":
    output = num1+num2
elif opt == "-":
    output = num1-num2
elif opt == "*":
    output = num1*num2
elif opt == "/":
    output = num1/num2
else:
    print("you enter wrong operator")

print("Your output is here:",output)

if num1 > num2:
    print("The number1 is greater than number2")
elif num1 == num2:
    print("The number is eual to 3")
else:
    print("The number is less than number2")

