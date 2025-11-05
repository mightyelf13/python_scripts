import sys
def turn_left(dx, dy):
    return dy, -dx

def turn_right(dx, dy):
    return -dy, dx

def is_open_space(labyrinth, x, y):
    return 0 <= y < len(labyrinth) and 0 <= x < len(labyrinth[y]) and labyrinth[y][x] == '.'

def update_labyrinth(labyrinth, old_position, new_position, dx, dy):
    old_x, old_y = old_position
    new_x, new_y = new_position

    labyrinth[old_y][old_x] = '.'

    orientations = {(0, -1): '^', (1, 0): '>', (0, 1): 'v', (-1, 0): '<'}
    labyrinth[new_y][new_x] = orientations[(dx, dy)]

def find_beast(labyrinth):
    for y, row in enumerate(labyrinth):
        for x, cell in enumerate(row):
            if cell in '^>v<':
                directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
                return (x, y), directions[cell]
    return None, None
def print_labyrinth(labyrinth):
    for row in labyrinth:
        print(''.join(row))
    print()
def move_beast(labyrinth, position, direction, N):
    x, y = position
    dx, dy = direction

    for _ in range(N):
        right_dx, right_dy = turn_right(dx, dy)

        if is_open_space(labyrinth, x + right_dx, y + right_dy):
            dx, dy = right_dx, right_dy
        elif is_open_space(labyrinth, x + dx, y + dy):
            x, y = x + dx, y + dy
        else:
            dx, dy = turn_left(dx, dy)

        update_labyrinth(labyrinth, position, (x, y), dx, dy)
        position = (x, y)

        print_labyrinth(labyrinth)

def read_input_from_keyboard():
    N = int(input())
    labyrinth = []
    while True:
        try:
            line = sys.stdin.readline()
            line = line.strip()
            if line == "":
                break
            labyrinth.append(list(line))
        except EOFError:
            break
    return N, labyrinth


# Main execution
N, labyrinth = read_input_from_keyboard()
beast_position, beast_direction = find_beast(labyrinth)
move_beast(labyrinth, beast_position, beast_direction, N)

