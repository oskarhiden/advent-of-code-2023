import time
import os

path = os.getcwd() + '/inputs/'
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