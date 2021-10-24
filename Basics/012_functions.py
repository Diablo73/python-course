def sumCal(a, b):
	return "Sum = " + str(a + b)


def subCal(a, b):
	return "Subtraction = " + str(a - b)


def mulCal(a, b):
	return "Multiplication = " + str(a * b)


def divCal(a, b):
	return "Division = " + str(a / b)


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(sumCal(num1, num2))
print(subCal(num1, num2))
print(mulCal(num1, num2))
print(divCal(num1, num2))
