#Exercise 1

#Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?

import math

def binary_search(n):
    if n <=0:
        return 0
    return math.ceil(math.log2(n))+1

list_size=128
steps=binary_search(list_size)
print(f'Maximum steps for binary search list of {list_size} items: {steps}')

#______________________________________________________________________________________________
#Exercise 1.2

#Suppose you double the size of the list. What’s the maximum number of steps now?

import math

def binary_search_steps(n):

    steps_before = math.ceil(math.log2(n))  # Steps for n elements
    steps_after = math.ceil(math.log2(2 * n))  # Steps for 2n elements
    return steps_before, steps_after

# Example
n = 100  # Example list size
steps_before, steps_after = binary_search_steps(n)
print(f"Steps for size {n}: {steps_before}")
print(f"Steps for doubled size {2*n}: {steps_after}")

#__________________________________________________________________________________________________
#Exercise

#1.3 You have a name, and you want to fnd the person’s phone number in the phone book.
#1.4 You have a phone number, and you want to fnd the person’s name in the phone book. (Hint: You’ll have to search through the wholebook!)
#1.5 You want to read the numbers of every person in the phone book.
#1.6 You want to read the numbers of just the As

#1.3 - Answer
def find_phone_book(phone_book, name):
    if name in phone_book:
        return f"{name}'s phone number is {phone_book[name]}"
    else:
        return f"{name} is not in the phone book"

# Example
phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}
name_to_find = "Alice"
print(find_phone_book(phone_book,name_to_find))

name_to_find = "Eve"
print(find_phone_book(phone_book,name_to_find))


#1.4 - Answer
def find_name_by_phone_number(phone_book, phone_number):
    
    for name, number in phone_book.items():  # Fix: use 'number' instead of 'phone_number' in the loop
        if number == phone_number:
            return f"The phone number {phone_number} belongs to {name}."
    return f"Sorry, the phone number {phone_number} is not in the phone book."


# Example usage
phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

# Test Cases
phone_number_to_find = "987-654-3210"
print(find_name_by_phone_number(phone_book, phone_number_to_find))
phone_number_to_find = "111-222-3333"
print(find_name_by_phone_number(phone_book, phone_number_to_find))

#1.5 - Answer

def list_all_numbers(phone_book):
    return list(phone_book.values())

#Example
phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

all_numbers = list_all_numbers(phone_book)
print("All phone numbers in the phone book:")
for number in all_numbers:
    print(number)

#1.6

def list_numbers_of_A(phone_book):
    numbers_of_A = [number for name, number in phone_book.items() if name.startswith("A")]
    return numbers_of_A

phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555",
    "Angela": "111-222-3333",
}
numbers_of_A = list_numbers_of_A(phone_book)
print("The phone numbers of people whose names start with 'A' in the phonebook:")

for number in numbers_of_A:
    print(number)
