def calculator(num1, num2, operation):
	result = 0

	if operation == "+" or operation.lower() == "a":
		result = sumCal(num1, num2)
	elif operation == "-" or operation.lower() == "s":
		result = subCal(num1, num2)
	elif operation == "*" or operation.lower() == "m":
		result = mulCal(num1, num2)
	elif operation == "/" or operation.lower() == "d":
		result = divCal(num1, num2)

	print(result)
	print("\n--------------------------------------------\n")


def sumCal(a, b):
	return "Sum = " + str(a + b)


def subCal(a, b):
	return "Subtraction = " + str(a - b)


def mulCal(a, b):
	return "Multiplication = " + str(a * b)


def divCal(a, b):
	return "Division = " + str(a / b)


if __name__ == '__main__':
	allowedOperations = ["a", "s", "m", "d", "A", "S", "M", "D", "+", "-", "*", "/"]
	while True:
		operation = input("Enter operation: ")
		if operation not in allowedOperations:
			break
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		calculator(num1, num2, operation)

print("\nBYE")
