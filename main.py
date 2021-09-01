lettersA = {"A", "B", "C", "D"}
lettersB = {"A", "E", "F"}
union = lettersA | lettersB  # Add them together, order not guaranteed
intersection = lettersA & lettersB  # What occurs in both
difference = lettersA - lettersB  # What occurs in lettersA but not in lettersB

print(f"Union {union}")
print(f"Intersection {intersection}")
print(f"Difference {difference}")
