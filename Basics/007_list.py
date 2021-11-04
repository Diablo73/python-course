a = [1, 2, 4, 8, 6, 7, 10, 5, 20, 9]
print(a[7])
print(a)

a[4] = a[9]
a.append(100)
print(*a)

a.sort()
print(*a)

a.reverse()
a.pop(2)
print(*a)

print(a.count(9))
a.remove(9)
a.insert(4, 33)
print(*a)
print(a[2:5])

print(a.index(33))
print(a.index(33, 3, 6))

print(sum(a))
a.clear()
print(a)
