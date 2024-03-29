import os
import random

def generate_layout(size, min_width, max_width, min_height, max_height, min_food_percentage, max_food_percentage, min_ghosts, max_ghosts):
    width = random.randint(min_width, max_width)
    height = random.randint(min_height, max_height)

    layout = [[' ' for _ in range(width)] for _ in range(height)]

    # Place walls
    for i in range(width):
        layout[0][i] = layout[height - 1][i] = '%'
    for i in range(height):
        layout[i][0] = layout[i][width - 1] = '%'
    
    # Place walls randomly inside the layout
    num_walls = random.randint(10, 30)  # Adjust this range as needed
    for _ in range(num_walls):
        x, y = random.randint(1, width - 2), random.randint(1, height - 2)
        layout[y][x] = '%'

    # Place Pacman
    pacman_pos = (random.randint(1, height - 2), random.randint(1, width - 2))
    layout[pacman_pos[0]][pacman_pos[1]] = 'P'

    # Place food items
    total_blocks = (width - 2) * (height - 2)
    food_percentage = random.randint(min_food_percentage, max_food_percentage)
    num_food_items = int((total_blocks * food_percentage) / 100)
    for _ in range(num_food_items):
        while True:
            x, y = random.randint(1, width - 2), random.randint(1, height - 2)
            if layout[y][x] == ' ':
                layout[y][x] = '.'
                break

    # Place ghosts
    num_ghosts = random.randint(min_ghosts, max_ghosts)
    for _ in range(num_ghosts):
        while True:
            x, y = random.randint(1, width - 2), random.randint(1, height - 2)
            if layout[y][x] == ' ':
                layout[y][x] = 'G'
                break

    return layout

def save_layout(layout, size, index):
    folder = f"layouts/{size}"
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/{size}_layout_{index}.lay"
    with open(filename, 'w') as f:
        for row in layout:
            f.write(''.join(row) + '\n')

sizes = {
         'large': (20, 35, 10, 20, 60, 80, 1, 4)}

for size, params in sizes.items():
    print(f"Generating {size} layouts...")
    min_width, max_width, min_height, max_height, min_food, max_food, min_ghosts, max_ghosts = params
    for i in range(1, 101):
        layout = generate_layout(size, min_width, max_width, min_height, max_height, min_food, max_food, min_ghosts, max_ghosts)
        save_layout(layout, size, i)
        print(f"Layout {i} generated for {size}.")

print("Layout generation completed.")
