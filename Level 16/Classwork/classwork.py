# Task1.

names = ["gio", "luka", "levani", "beqa", "gabriel"]
print(names[1:4])

# Task2.

names = ["gio", "luka", "levani", "beqa", "gabriel", "lile"]
x = []
x.append(names[0:3])
print(x)

# Task3.

names = ["gio", "luka", "levani", "beqa", "gabriel", "lile"]
x = names.index("gio")
print(x)
x = names.index("luka")
print(x)
x = names.index("levani")
print(x)

# Task4.

numbers = [1, 2, 3, 4, 5]
x = max(numbers)

y = min(numbers)

numbers.remove(x)
numbers.remove(y)
print(numbers)

# Task5.

new_numbers = []
new_numbers.append(x)
new_numbers.append(y)
print(new_numbers)

# Task6.

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [2, 5, 3, 4, 7,]

min_list1 = min(numbers1)
max_list1 = max(numbers1)

min_list2 = min(numbers2)
max_list2 = max(numbers2)

result1 = max_list2 - min_list1
result2 = max_list1 - min_list2

new_list = [result1, result2]
print(new_list)

# Task7.

numbers = [1, 2, 3, 4, 5]
sum = sum(numbers)
print(sum)

# Task8.  [Unfinished]

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


# Task9.

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [2, 5, 2, 6, 4]

sum1 = sum(numbers1)
sum2 = sum(numbers2)

print(sum1)
print(sum2)

# Task10.

list = ["luka", "gio", "nika", "nia", "lile"]
reversed_list = list[::-1]
print(reversed_list)

# Task11.

name = "LUKA"
reversed_name = name[::-1]
print(reversed_name)






















