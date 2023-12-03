import os 

path = os.getcwd() + '/inputs/'
filename = 'input-dec2.txt'

with open(path + filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

dict_cubes = {
    'red': 12,
    'blue': 14,
    'green': 13,
}

def valid_game(subset_cubes):
    for set in subset_cubes:
        set = set.split(',')
        for cube_col in set:
            cube = cube_col.split(' ')
            nr = int(cube[1])
            color = cube[2]
            if nr > dict_cubes[color]:
                return False
    return True

sum = 0
for game in content:
    game = game.split(':')
    game_nr = int(game[0].split(' ')[1])
    subset_cubes = game[1].split(';')
    
    if valid_game(subset_cubes):
        sum = sum + game_nr

print(sum)


print('------------------')
print('     part 2')
print('------------------')
        
def update_max_col(set, max_col):
    for cube_col in set:
        cube = cube_col.split(' ')
        nr = int(cube[1])
        color = cube[2]
        if nr > max_col[color]:
            max_col[color] = nr

def power_set_of_game(subset_cubes):
    max_col = {
        'red': 0,
        'blue': 0,
        'green': 0,
    }
    for set in subset_cubes:
        set = set.split(',')
        update_max_col(set, max_col)
    return max_col['red'] * max_col['blue'] * max_col['green']
    

sum = 0
for game in content:
    game = game.split(':')
    game_nr = int(game[0].split(' ')[1])
    subset_cubes = game[1].split(';')
    
    sum += power_set_of_game(subset_cubes)

print(sum)