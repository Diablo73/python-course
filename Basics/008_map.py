a = {"a": 1, "b": 2, "c": 3, "l": [10, 23, 13]}
print(a)
print(a["b"])
print(a["l"][1])

print(a.get("l"))
print(*a.keys())
print(*a.values())
b = a.values()
print(*b)

a["b"] = 50
print(a)

a.pop("b")
print(a)
