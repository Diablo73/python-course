a = 15

for i in range(1, 101):
	if i % 7 == 0:
		continue
	if a * i > 150:
		break
	print(a, "*", i, "=", a * i)
