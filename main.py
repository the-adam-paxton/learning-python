def greet(name, age=-1):
    print(f"Hello {name}, how are you?")
    if age >= 0:
        print(f"My god you are {age} years old!")


def is_adult(age):
    return age >= 16


def convert_gender(gender="unknown"):
    gender = gender.upper()
    if gender == "M":
        return "Male"
    elif gender == "F":
        return "Female"
    else:
        return f"Gender {gender} is unknown"

greet("Adam", 39)
greet("Mila")

result = is_adult(16)
print(result)

print(convert_gender("m"))
print(convert_gender("hello"))