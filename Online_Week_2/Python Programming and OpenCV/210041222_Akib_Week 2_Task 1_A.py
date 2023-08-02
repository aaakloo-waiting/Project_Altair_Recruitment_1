# Implementing function from given instructions and grid size of robot movement

instructions = input("Enter instructions: ")  # input() takes only string input
grid_size_str = input("Enter a grid size: ")
grid_size = eval(grid_size_str)  # eval() is a powerful fn to convert string to any python dynamic expression


def process_instructions(instructions, grid_size):
    direction = 'N'
    x = 0
    y = 0
    for instruction in instructions:
        if direction == 'N':
            if instruction == 'F':
                y += 1
            elif instruction == 'L':
                direction = 'W'
            elif instruction == 'R':
                direction = 'E'
        elif direction == 'W':
            if instruction == 'F':
                x -= 1
            elif instruction == 'L':
                direction = 'S'
            elif instruction == 'R':
                direction = 'N'
        elif direction == 'S':
            if instruction == 'F':
                y -= 1
            elif instruction == 'L':
                direction = 'E'
            elif instruction == 'R':
                direction = 'W'
        elif direction == 'E':
            if instruction == 'F':
                x += 1
            elif instruction == 'L':
                direction = 'N'
            elif instruction == 'R':
                direction = 'S'
        # Checking the boundary
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if y > int(grid_size[1]):
            y = int(grid_size[1])
        if x > int(grid_size[0]):
            x = int(grid_size[0])

    result = (x, y, direction)
    return result


# Showing result
print(process_instructions(instructions, grid_size))
