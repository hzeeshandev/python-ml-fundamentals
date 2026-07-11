# Takes a marks variable and prints a grade using if/elif/else (use the scale above or your own)
marks = 71
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")  
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

#Uses a for loop to print all numbers from 1 to 20 that are divisible by 3
for i in range(1, 21):
    if i % 3 == 0:
        print(i)

#Uses a while loop to print a countdown from 10 to 1, then prints "Liftoff!"
count = 10
while count >= 1:
    print(count)
    count -= 1
print("Liftoff!")

#Uses break inside a loop to stop searching a list once a target value is found — e.g. search [4, 8, 15, 16, 23, 42] for 23 and print "Found it!" once located
numbers = [4, 8, 15, 16, 23, 42]
for num in numbers:
    if num == 23:
        print("Found it!")
        break