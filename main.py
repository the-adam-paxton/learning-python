brand = 'Amigoscode'
print(brand.replace('A','a'))
print(len(brand))
print(brand == 'Amigoscode')
print('code' not in brand)

name = "Jamila"
email = """
Hello {},
How are you? 
It was nice talking to you
"""

print(email.format(name))

age = 22
note = f"""
Hello {name},
You never told me you are {age}!
"""

print(note)