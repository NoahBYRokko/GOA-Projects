# Task1.

fav_cars = []
for i in range(5):
    cars = input("Enter the name of your favourite car brand: ")
    fav_cars.append(cars)
print(fav_cars)

# Task2. 

fav_animes = ["Attack On Titan", "HxH", "JoJo", "Code Geass", "Berserk"]
print(fav_animes[2])

# Task3.

info = ["Bachi", 2009, "JoJo", "Volleyball", "Programing"]
info[1] = 14
print(info)

# Task4.

fruits = ["Banana", "Apple", "Peach", "Grape", "Pineapple"]
fruits.append("Strawberry")
fruits.remove("Apple")
print(fruits)

# Task5.
# 1:
numbers = [1,2,14,0,5,6,-8]
min_number = numbers[0]

for number in numbers:
    if min_number > number:
        min_number = number

print(min_number)

# 2:

numbers = [1,2,14,0,5,6,-8]
max_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number

print(max_number)

# 3:

numbers = [1,2,14,0,5,6,-8]
sum_numbers = 0

for number in numbers:
    sum_numbers = sum_numbers + number

# Task6.
 
name_list = []
for i in range(5):
    names = input("Enter any name: ")
    name_list.append(names)
x = name_list.count("luka")
print(x)

# Task7.

numbers = [1, 2, 3, 4, 5]

numbers.pop()

numbers.pop(0)

print(numbers)
