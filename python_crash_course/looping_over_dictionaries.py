person = {"name": "Alice", "age": 30, "job": "Engineer"}

# for key in person:
#     print(key)

# print(person.values())

# for value in person.values():
#     print(value)

# print(person.items())

for key, value in person.items():
    output = f"{key}: {value}"
    print(output)
