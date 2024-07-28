# Task1.

def greet():
    print("Welcome.")

greet()

# Task2.
print("__________________Task2.__________________")

def greet():
    x = (input("Please enter your name: "))
    print("Welcome" + " " +  x)

greet()

# Task3.
print("__________________Task3.__________________")

def odd_even(number_list):
    for i in number_list:
        if i % 2 == 0:
            print(str(i) + " is even")
        else:
            print(str(i) + " is odd")


odd_even([1, 2, 3, 4, 5])
    