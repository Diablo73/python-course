if __name__ == '__main__':
	number = input("Enter number: ")
	sumOfDigits = 0
	li = list(number)
	li = [int(i) for i in li]

	print(sum(li))

	number = int(number)
	while number > 0:
		digit = number % 10
		sumOfDigits += digit
		number //= 10

	print(sumOfDigits)
