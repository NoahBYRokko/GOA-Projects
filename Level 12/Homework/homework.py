# Task 1...5 [Finished]

# Task6.

num = int(input("Please enter any number between 1 and 7: "))
if num == 1:
    print("It's Monday.")
elif num == 2:
    print("It's Tuesday.")
elif num == 3:
    print("It's Wednesday.")
elif num == 4:
    print("It's Thursday.")
elif num == 5:
    print("It's Friday.")
elif num == 6:
    print("It's Saturday.")
else:
    print("It's Sunday.")

# Task7.

i = 0
while i <= 10:
    if i % 2 == 0:
        print(str(i) + "is Even")
    else:
        print(str(i) + "is Odd")
    i = i + 1

# Task8.

age = int(input("Please enter your age: "))
if age >= 5 and age <= 12:
    print("Your are a child.")
elif age >= 12 and age <= 18:
    print("Your are a teenager.")
elif age > 18:
    print("Your are an adult.")

# Task9.

budget = int(input("Please enter your budget amount: "))
if budget >= 300:
    print("You can buy the item you've picked. ")
else:
    print("You don't have enough budget to buy the item. ")

# Task10. [Finished]

# Task11. 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

i = int(input("Please enter your choice (1/2/3/4): "))
if i == 1:
    print(num1 + num2)
elif i == 2:
    print(num1 - num2)
elif i == 3:
    print(num1 * num2)
elif i == 4:
    print(num1 / num2)
else:
    print("Invalid Operation")



# Task12. 

i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i = i + 1
    print(sum)











