import time
import os
import re
import pandas as pd

#path = os.getcwd() + '/inputs/'
path =  'inputs/'
filename = 'input-dec1.txt'

with open(path + filename) as f:
    content = f.readlines()

content = [x.strip() for x in content]

# content = content[:3]
# print(content)
sum = 0 
for row in content:
    # keep only numbers in each string i 
    for s in row:
        if s.isdigit():
            number1 = int(s)*10
            break
    for s in reversed(row):
        if s.isdigit():
            number2 = int(s)
            break
    sum = sum + (number1 + number2)
print('total sum:', sum)
    # concat

print('------------------')
print('     part 2')
print('------------------')

start_time = time.time()
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
values = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_len = []
for number in numbers:
    numbers_len.append(len(number))

def get_value(word, start='begining'):
    letter_idx = range(len(word)) if start=='begining'  else range(len(word)-1, -1, -1)
    for i in letter_idx:
        for j in range(len(numbers)):
            if word[i:i+numbers_len[j]] == numbers[j]:
                return values[j]

sum = 0
for row in content:
    number1 = get_value(row)
    number2 = get_value(row, 'end')
    sum = sum + (number1*10 + number2)

print('total sum:', sum)
print("--- %s seconds ---" % (time.time() - start_time))

print('------------------')
print('   part 2 test')
print('------------------')
start_time = time.time()
number_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9
}

def get_value(word, start='begining'):
    letter_idx = range(len(word)) if start=='begining'  else range(len(word)-1, -1, -1)
    for i in letter_idx:
        for j in range(6):
            prop = number_dict.get(word[i:i+j], 0)
            if prop != 0:
                return prop

sum = 0
for row in content:
    number1 = get_value(row)
    number2 = get_value(row, 'end')
    sum = sum + (number1*10 + number2)

print('total sum:', sum)
print("--- %s seconds ---" % (time.time() - start_time))




exit()

def main():
    inp = read_input()
    start_time = time.time()
    array_of_nums = []
    for _, row in inp.iterrows():
        numbers = _extract_nums(row["line"])
        (first, last) = _extract_first_last(numbers)
        array_of_nums.append(int(first + last))
    res = sum(array_of_nums)
    print(res)
    print("--- %s seconds ---" % (time.time() - start_time))    
    return res


def read_input():
    inp = pd.read_csv("inputs/input-dec1.txt", delimiter=" ", header=None, names=["line"])
    return inp


def _find_numbers(row):
    letter_to_dig_dict = {
        "one": "on1e",
        "two": "tw2o",
        "three": "thr3ee",
        "four": "fo4ur",
        "five": "fi5ve",
        "six": "si6x",
        "seven": "sev7en",
        "eight": "eig8ht",
        "nine": "ni9ne",
    }
    for number in letter_to_dig_dict.keys():
        row = row.replace(number, letter_to_dig_dict[number])
    return row


def _extract_nums(row):
    row_with_numbers = _find_numbers(row)
    return re.sub("[a-z]", "", row_with_numbers)


def _extract_first_last(numbers):
    first = numbers[0]
    last = numbers[-1]
    return (first, last)


main()