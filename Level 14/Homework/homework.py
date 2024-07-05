'''Pop:

1)Remove and print the last element of a list of integers.

2)Remove and return the first element of a list of strings.

3)Pop the element at index 2 from a list of characters.

4)Remove and return the last element of a list of tuples.

5)Handle IndexError by popping from an empty list.'''

# 1:
numbers = [1, 2, 3, 4, 5]
x = numbers.pop()
print(x)

# 2:
names = ["Gio", "Alex", "Luka",]
x = names.pop(0)
print(x)

# 3:

x = [6, True, "Hello", "Audi", "Luka"]
y = x.pop(1)
print(y)

# 4:

Xtuples = ["banana", "apple", "peach"]
y = Xtuples.pop()
print(y)

# 5:   [Unfinished]

fruits = [2 ]
fruits.pop()


'''Count:

1)Count how many times the number 5 appears in a list of integers.

2)Count occurrences of the letter 'a' in a list of strings.

3)Count the number of True values in a list of boolean values.

4)Count occurrences of a sublist [3, 4] in a nested list.'''

# 1:

int_list = [1, 2, 3, 4, 5, 5]
x = int_list.count(5)
print(x)

# 2:

fruits = ["banana", "cherry", "apple", "pineapple"]
x = fruits.count("a")
print(x)

# 3:

boolean_list = [True, True, False, True, False]
x = boolean_list.count(True)
print(x)

# 4: [Unfinished]


'''Max:

1)Find the maximum number in a list of integers.

2)Find the maximum string length in a list of strings.

3)Find the oldest person's age in a list of ages.

4)Find the most recent date in a list of datetime objects.'''

# 1:
numbers = [1, 2, 3, 4, 5]
max_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number

print(max_number)

# 2:

fruits = ["banana", "cherry", "pineapple", "apple"]
max_length = max(len(s) for s in fruits)
print(max_length)

# 3:

age = [20, 25, 30, 50, 60]
max_age = age[0]

for age in age:
    if max_age < age:
        max_age = age

print(max_age)

# 4:
from datetime import datetime

dates = [datetime(2022, 1, 1), datetime(2022, 2, 15), datetime(2022, 3, 20), datetime(2022, 1, 10)]
most_recent_date = max(dates)
print(most_recent_date)

'''Min:

1)Find the smallest number in a list of integers.

2)Find the shortest word in a list of strings.

3)Find the lowest temperature in a list of daily temperatures.

4)Find the minimum price in a list of products.'''

# 1:

numbers = [1, 2, 3, 4, 5]
min_number = numbers[0]

for number in numbers:
    if min_number > number:
        min_number = number

print(min_number)

# 2:

fruits = ["banana", "cherry", "pineapple", "apple"]
min_length = min(len(s) for s in fruits)
print(min_length)

# 3:

temperature = [10, 15, 19, 20, 30]
min_temperature = temperature[0]

for temperature in temperature:
    if temperature > temperature:
        min_temperature = temperature

print(min_temperature)

# 4:

price = [2.59, 3, 5.69, 10]
min_price = price[0]

for price in price:
    if min_price > price:
        min_price = price

print(min_price)

'''Sum:

1)Calculate the sum of all numbers in a list of integers.

2)Calculate the total length of strings in a list of strings.

3)Calculate the total score of a team in a list of game results.

4)Sum the elements of nested lists to get a flattened sum.'''

# 1:

numbers = [1, 2, 3, 4, 5]

sum_numbers = 0

for number in numbers:
    sum_numbers = sum_numbers + number
print(sum_numbers)

# 2:

fruits = ["banana", "cherry", "apple", "pineapple"]
total_length = sum(len(s) for s in fruits)
print(total_length)

# 3:

game_results = []
team_scores = {"Team A": 0, "Team B": 0}

for game in game_results:
    if game["home_team"] in team_scores:
        team_scores[game["home_team"]] += game["home_score"]
    else:
        team_scores[game["away_team"]] += game["away_score"]

print("Total scores:", team_scores)

# 4:

def sum_nested_list(lst):
    result = 0
    for elem in lst:
        if isinstance(elem, list):
            result += sum_nested_list(elem)
        else:
            result += elem
    return result

nested_list = [1, 2, [3, 4], [5, [6, 7], 8]]
print(sum_nested_list(nested_list))

'''Len:

1)Find the length of a list of 10 random integers.

2)Determine the number of elements in a list of strings representing weekdays.

3)Calculate the length of a nested list.'''

# 1:

numbers = [1, 2, 3, 4, 5]
print(len(numbers))

# 2:

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(len(weekdays))

# 3:

nested_list = [1, 2, [3, 4], [5, [6, 7], 8]]
print(len(nested_list))
