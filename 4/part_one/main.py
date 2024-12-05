from enum import Enum

def get_next_coordinate(x, y, way):
    if way == 'UP':
        return x,y-1
    if way == 'DOWN':
        return x,y+1
    if way == 'LEFT':
        return x-1,y
    if way == 'RIGHT':
        return x+1,y
    if way == 'DOWN-RIGHT':
        return x+1,y+1
    if way == 'DOWN-LEFT':
        return x-1,y+1
    if way == 'UP-RIGHT':
        return x+1,y-1
    if way == 'UP-LEFT':
        return x-1,y-1

def create_array(content: str):
    input_lines = content.splitlines()
    data = []
    for line in input_lines:
        data_line = []
        for char in line:
            data_line.append(char)
        data.append(data_line)
    return data

def get_char(array, x, y):
    return array[y][x]

def check_way_string(array, line, column, way, check_against):
    x = column
    y = line
    for char in check_against:
        if y < 0 or y >= len(array) or len(array[y]) <= x or x < 0:
            return False
        c = get_char(array, x, y)
        if c != char:
            return False
        x,y = get_next_coordinate(x, y, way)
    print(f'{ check_against } at { column }, { line } { way } ')
    return True

def check_ways_string(array, line, column, check_against):
    count = 0
    if get_char(array, column, line) == check_against[0]:
        for way in ['UP', 'DOWN', 'LEFT', 'RIGHT', 'DOWN-RIGHT', 'DOWN-LEFT', 'UP-RIGHT', 'UP-LEFT']:
            if check_way_string(array, line, column, way, check_against):
                count += 1
    return count

def main():
    content = ''
    with open('input.txt', 'r') as file:
        content = file.read()
    data_array = create_array(content)
    count = 0
    for line in range(len(data_array)):
        for column in range(len(data_array[line])):
            #print (line,column, data_array[line][column])
            count += check_ways_string(data_array, line, column, 'XMAS')
    print(count)

if __name__ == '__main__':
    main()