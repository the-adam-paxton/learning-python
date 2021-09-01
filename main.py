names = ["Ahmed", "Anna", "James", "Jamila"]

# For loop works with list or set
for person in names:
    print(person)

person = {
    "name": "Adam",
    "age": 39,
    "address": "GB"
}

for key in person:
    print(f"key:{key} value:{person[key]}")

for key, value in person.items():
    print(f"key:{key} value:{value}")

print(person.items())


# EXERCISE - add numbers in the list
numbers = [2, 4, 6, 8]

result = 0
for i in numbers:
    result += i

print(f"Result = {result}")
