if __name__ == '__main__':
	principle = float(input("Enter principle: "))
	rate = float(input("Enter rate: "))
	year = float(input("Enter year: "))

	simple_interest = (principle * rate * year) / 100

	print(simple_interest)
