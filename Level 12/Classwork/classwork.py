# Task1.

i = 20
while i >= 1:
    print(i)
    i = i - 1

# Task2.

i = 0
while i <= 10:
    print(i)
    i = i + 2

# Task3.

i = 1
sum = 0
while i <= 10:
    sum = sum + 1
    i = i + 1

# Task4.

correct_password = "167069"
user_input = ""
while correct_password != user_input:
    user_input = input("Please enter your password: ")
    if user_input == correct_password:
        print("You have successfuly logged in.")
    else:
        print("Password is incorrect.")

# Task5.

i = 1
while i <= 9:
    print(i)
    i = i + 2

# Task6. 

age = (int(input("Please enter your age: ")))

if age < 18:
    print("You can't enter the program")

while age < 18:
    int(input("Please enter your age: "))

# Task7.

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

# Task8.

i = 0
while i <= 10:
    if i % 2 == 0:
        print(str(i) + "is Even")
    else:
        print(str(i) + "is Odd")
    i = i + 1

# Task9.

age = int(input("Please enter your age: "))
if age >= 5 and age <= 12:
    print("Your are a child.")
elif age >= 12 and age <= 18:
    print("Your are a teenager.")
elif age > 18:
    print("Your are an adult.")

# Task10.

age = int(input("Please enter your age: "))
if age >= 18:
    print("You can participate in an erection")
else:
    print("You cant participate in an eraction")













