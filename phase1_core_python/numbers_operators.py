#Takes two numbers (pick any values), and prints their sum, difference, product, and floor division result

a = 30
b = 70
print(a + b)
print(a - b)
print(a * b)
print(a // b)

#Checks if a given number is even or odd using %, and prints a message like "15 is odd"

if a % 2 == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")

#Takes a float like 9.86 and prints both the truncated int version and the rounded version

x = 9.86
print(f"int version of x is {int(x)} and rounded version of x is {round(x)}")

#Uses an augmented assignment operator to increase a price variable by 20%, then prints the new price
y = 300
y *= 1.2
print(y)