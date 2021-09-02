number = 0

print("While continue example")
while number < 10:
    number += 1
    if number < 5:
        continue
    print(number)

number = 0
print("While break example")
while number < 10:
    if number == 5:
        break
    number += 1
    print(number)

print("For continue example")
for n in [1, 2, 3, 4, 5, 6, 7]:
    if n < 5:
        continue
    print(n)

print("For break example")
for n in [3, 4, 5, 6, 7, 8, 9]:
    if n >= 5:
        break
    print(n)
