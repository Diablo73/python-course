# a = int(input("Enter your name: "))

# print(a + 5)

b = input("Enter list: ").split(" ")

print(b)
c = []
for i in b:
	c.append(int(i))
print(sum(c))

b = [int(i) for i in b]

print(b)
print(sum(b))
