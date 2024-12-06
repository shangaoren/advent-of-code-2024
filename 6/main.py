

def create_map():
    content = ''
    with open('input.txt', 'r') as file:
        content = file.read()
    area_map = []
    for line in content.splitlines():
        current_line = []
        for column in line:
            current_line.append(column)
        area_map.append(current_line)
    return area_map

def get_tile(area, x,y):
    return area[y][x]

def set_tile(area,x, y, symbol):
    area[y][x] = symbol

def get_start_direction(area, x, y):
    start_symbol = get_tile(area,x,y)
    if start_symbol == '<':
        return 'LEFT'
    if start_symbol == '>':
        return 'RIGHT'
    if start_symbol == 'v':
        return 'DOWN'
    if start_symbol == '^':
        return 'UP'
    raise Exception('Symbol is not a direction')

def move_cursor(x,y, direction):
    if direction == 'LEFT':
        return x-1,y
    if direction == 'RIGHT':
        return x+1,y
    if direction == 'UP':
        return x,y-1
    if direction == 'DOWN':
        return x,y+1
    raise Exception('Direction is not valid')

def count_x_s(area):
    count = 0
    for line in area:
        for char in line:
            if char == 'X':
                count += 1
    return count

def rotate(direction):
    if direction == 'LEFT':
       return 'UP'
    if direction == 'RIGHT':
        return 'DOWN'
    if direction == 'UP':
        return 'RIGHT'
    if direction == 'DOWN':
        return 'LEFT'
    raise Exception('Direction is not valid')

def find_start_point(area_map):
    for y in range(len(area_map)):
        for x in range(len(area_map[y])):
            current_symbol = area_map[y][x]
            if current_symbol in ['<', '>', 'v', '^']:
                return x,y
    raise Exception('No start point found')

def main():
    area_map = create_map()
    start_x, start_y= find_start_point(area_map)
    start_direction = get_start_direction(area_map, start_x, start_y)
    print(f' start point: {start_x}, {start_y}')
    x:int = start_x
    y:int = start_y
    direction = start_direction
    end_found = False
    while end_found is False:
        set_tile(area_map,x,y,'X')
        next_x, next_y = move_cursor(x,y,direction)
        if 0 <= next_x < len(area_map) and 0 <= next_y < len(area_map):
            if get_tile(area_map,next_x,next_y) == '#':
                direction = rotate(direction)
            else:
                x = next_x
                y = next_y
        else :
            end_found = True
    print(count_x_s(area_map))
    return True

if __name__ == "__main__":
    main()