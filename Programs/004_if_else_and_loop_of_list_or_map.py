li = [1, 2, 4, 8, 6, 7, 10, 5, 20, 9]
m1 = {"a": 15, "b": 22, "c": 37, "d": 15}
m2 = {1: 15, 2: 22, 3: 37}

print(sum(li))
print(sum(m2))
print(sum(m1.values()))

a = 0
b = 1
for i in li:
	a = a + i
	b = b * i
print(a, b)

a = 0
b = 1
for i in m1.values():
	a = a + i
	b = b * i

print(a, b)

if 7 in li:
	print(7)
if 70 not in li:
	print(70)
if "a" in m1:
	print(m1["a"])
