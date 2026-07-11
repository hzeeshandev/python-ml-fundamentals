# Creating strings

name = "Zeeshan"
message = 'this is python tutorial'
multiline = """this is multiline
comment"""
print(name)
print(message)
print(multiline)

# Indexing & Slicing

print(name[0])
print(name[3])
print(name[-1])
print(name[0:3])
print(name[:3])
print(name[3:])
print(name[::-1])

# Common String Methods

s = "  Hello World  "
print(s.strip())
print(s.split())
print(s.lower())
print(s.upper())
print(len(s))
print(s.startswith("  Hel"))
print(s.replace("World", "Zeeshan"))
print("-".join(["a","b","c"]))

#f-strings (the modern, correct way to format strings)

stud = "Zeesahn"
gpa = 2.5
age = 22
print(f"my name is {stud} and im {age} year old and my gpa is {gpa:.1f}.")
print(f"{stud.upper()} is a student.")

# Exercise

Name = "muhammad zeeshan ali"
print(Name.title())
first_name = Name.split()[0]
print(first_name)
print(len(Name))
print(f"Your name has {len(Name)} characters and starts with 'M'")