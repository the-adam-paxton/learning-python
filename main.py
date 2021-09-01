person = {
    "name": "Adam",
    "age": 20,
    "address": "USA"
}

print(person["name"])
print(person["age"])
print(person["address"])
print(person.keys())
print(person.values())
# person.clear()
person["age"] = 100
print(person)