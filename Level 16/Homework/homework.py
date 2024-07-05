# Task1.

numbers = [1, 2, 3, 4, 5]
min_number = numbers[0]

for number in numbers:
    if min_number > number:
        min_number = number

print("Smallest member:", min_number)

# Task2.

numbers = [1, 2, 3, 4, 5]
max_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number

print("Biggest Member:", max_number)

# Task3.

numbers = [1, 2, 3, 4, 5, 6]
index1 = numbers.index(1)
index2 = numbers.index(3)
index3 = numbers.index(5)


print(index1, index2, index3)

# Task4.

names = ["luka", "gio", "nika", "nia", "lile"]
numbers = [1, 2, 3, 4, 5]

new_list = []
x = 0 
y = 0

while x < len(names) and y < len(numbers):
    new_list.append(numbers[y])
    new_list.append(names[x])
    x += 1
    y += 1

print(new_list)

# Task5.

list = [1, "luka", 2, "nia", 3, "nika", 4]

strings = []
integers = []


for i in list:
    if isinstance(i, str):
        strings.append(i)
    else:
        integers.append(i)

print("Strings:", strings)
print("Integers:", integers)

# Task6.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

even = []
odd = []

for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


for i in list2:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

sum1 = sum(even)
sum2 = sum(odd)


print("Sum of Even numbers:", sum1)
print("Sum of Odd numbers:", sum2)

# Task7.

list1 = [4, 6, 8, 9]
list2 = [2, 3, 7, 8]
list3 = [1, 5, 2, 4]
list4 = [3, 4, 1, 2]

even = []
odd = []


for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


for i in list2:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


for i in list3:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


for i in list4:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        

print("Even numbers:", even)
print("Odd numbers:", odd)

# Task8.

names = ["luka", "gio", "nika", "nia", "lile"]

new_names = []

for i in names:
    if isinstance(i, str):
        new_names.append((i, len(names)))

print(new_names)

# Task9. 

list = ["luka", 2, 3, 5, "gio", "nika", 1, "nia", 4, "lile"]

names = []
numbers = []

for i in list:
    if isinstance(i, str):
        names.append(i)
    else:
        numbers.append(i)
x = "".join(names)
print("Strings:", x)

sum = sum(numbers)
print("Sum of numbers:", sum)

# Task10.

numbers =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []

for i in range(len(numbers)):
    if i % 2 == 0:
        new_list.append(numbers[i])
    else:
        pass

print(new_list)
 
