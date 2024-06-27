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