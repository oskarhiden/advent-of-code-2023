import os 

path = os.getcwd() + '/inputs/'
filename = 'input-dec3.txt'

with open(path + filename) as f:
    content = f.readlines()

content = [x.strip() for x in content]
#content = content[:2]
# debug
# content = [
#     '467..114..',
#     '...*......',
#     '..35...633',
#     '......#...',
#     '617*......',
#     '.....+.58.',
#     '..592.....',
#     '......755.',
#     '...$.*....',
#     '.664.598..'
# ]
# for row in content:
#     print(row)


def is_digit(str):
    return True if str in(['0','1', '2', '3', '4', '5', '6', '7', '8', '9']) else False

def adjust_surounding_rows(i, row, current_row=False):
    adjust = 1
    if row is None:
        return '...'
    else:
        #print('--------------', row[max(i-adjust,0):(i+1+adjust)] )
        return row[max(i-adjust,0):(i+1+adjust)]
    
def holds_symbol(string):
    allowed = '.0123456789'
    for char in string:
        if char not in allowed:
            #print('true')
            return True
    return False

# for every digit of a number looka at sourounding symbols
# if not . or digit then the number is ok. 
def check_surounding(i, row, row_before=None, row_after=None):
    row = adjust_surounding_rows(i, row)
    row_before = adjust_surounding_rows(i, row_before)
    row_after = adjust_surounding_rows(i, row_after)
    # chek if other than number or .
    # print(row_before)
    # print(row)
    # print(row_after)
    # print()
    return holds_symbol(row + row_before + row_after)

def check_row(row, row_before=None, row_after=None):
    row_numbers = []
    # Find number on a row, 
    # print(row)
    number = 0
    valid_number = False
    for i, char in enumerate(row):
        
        if is_digit(char):
            valid_number = valid_number or check_surounding(i, row, row_before, row_after)
            number = number*10 + int(char)
        if not is_digit(char) or i == len(row)-1:
            # print('---------->',number)
            if valid_number:
                # print('---------->','valid')
                row_numbers.append(number)
            number = 0
            valid_number=False
    return row_numbers

print('>-----<')
s = 0
# print(len(content))
for row_nr in range(len(content)):
    #print(row_nr)
    if row_nr == 0:
        row_numbers = check_row(content[row_nr], row_after=content[row_nr+1])
    elif row_nr == len(content)-1:
        row_numbers = check_row(content[row_nr], row_before=content[row_nr-1])
    else:
        row_numbers = check_row(content[row_nr], row_before=content[row_nr-1], row_after=content[row_nr+1])
    # print(row_nr, ': ', row_numbers)
    s += sum(row_numbers)
print('=', s)


print('------------------')
print('     part 2')
print('------------------')

def get_entire_number(row, i):
    number = '' #row[i]
    number_idx = [] #[i]
    # check after digit
    for j, char in enumerate(row[i:]):
        if is_digit(char):
            number = number + char
            number_idx.append(i+j)
        else:
            break
    # check before digit
    for j, char in enumerate(row[i-1::-1]):
        # print(j, char)
        if is_digit(char):
            number = char + number
            number_idx.append(i-j-1)
        else:
            break
    return number, number_idx

def remove_number_from_row(row, number_idx):
    row = list(row)
    for idx in number_idx:
        row[idx] = '.'
    return ''.join(row)

def check_surounding_star(i, row):
    row_temp = row
    num_list = []
    for j in range(max(i-1,0), i+2):
        if is_digit(row_temp[j]):
            number, number_idx = get_entire_number(row_temp, j)
            num_list.append(int(number))
            # print('before', number, number_idx)
            # print(row_temp)
            row_temp = remove_number_from_row(row_temp, number_idx)
            # print(row_temp)
    return num_list

def check_row_star(row, row_before, row_after):
    all_n = []
    for i, char in enumerate(row):
        if char == '*':
            # print('star', i)
            l1 = check_surounding_star(i, row_before)
            l2 = check_surounding_star(i, row)
            l3 = check_surounding_star(i, row_after)
            # print( l1 + l2 + l3 )
            n = l1 + l2 + l3
            if len(n) > 2:
                raise Exception('more than 2 numbers')
            elif len(n) == 2:
                all_n.append( n[0] * n[1] )
                # print('n', n[0] * n[1])
    return all_n

s = 0
# print(len(content))
for row_nr in range(1, len(content)-1, 1):
    #print(row_nr)
    row_numbers = []
    if row_nr != 0 and row_nr != len(content)-1:
        row_numbers = check_row_star(content[row_nr], row_before=content[row_nr-1], row_after=content[row_nr+1])
    # print(row_nr, ': ', row_numbers)
    s += sum(row_numbers)
    
print('=', s)