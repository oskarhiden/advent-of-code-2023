import os 

path = os.getcwd() + '/inputs/'
filename = 'input-dec3.txt'

with open(path + filename) as f:
    content = f.readlines()

content = [x.strip() for x in content]
#content = content[:2]
# debug
content = [
    '467..114..',
    '...*......',
    '..35...633',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]
for row in content:
    print(row)


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