# Task1.
print("____________________Task1____________________")

def odd(integer_list):
    
    for i in integer_list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            pass

even_list = []        
odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(even_list)


# Task2.
print("____________________Task2____________________")

def odd_or_even(integer_list):
    odd_numbers = []
    even_numbers = []
    
    for i in integer_list:
        if i % 2 == 0:
            even_numbers.append(i /2)
        else:
            odd_numbers.append(i * 2)
    
    return odd_numbers, even_numbers


integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


odd_numbers, even_numbers = odd_or_even(integer_list)


print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
