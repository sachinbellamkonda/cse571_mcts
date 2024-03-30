import os
import random


def generate_layout(min_width, max_width, min_height, max_height, min_food_percentage, max_food_percentage,
                    min_ghosts, max_ghosts, weights, size, i):
    folder = f"layouts/{size}"
    os.makedirs(folder, exist_ok=True)
    f = open(f"layouts/{size}/{size}" + str(i) + ".lay", "w")
    length = random.randint(min_width, max_width)
    height = random.randint(min_height, max_height)
    totalBlocks = length * height
    randomFood = random.randint(min_food_percentage, max_food_percentage)
    foodItems = int((totalBlocks * randomFood) / 100)
    itemsLayout = [random.randint(1, length), "%", foodItems]
    pacmanPos = (random.randint(2, length - 2), random.randint(2, height - 2))
    noOfGhosts = random.randint(min_ghosts, max_ghosts)

    ghostNumbers = noOfGhosts
    ghostPos = []
    for i in range(ghostNumbers):
        indexGhost = (random.randint(2, length - 2), random.randint(2, height - 2))
        if pacmanPos == indexGhost or indexGhost in ghostPos:
            while pacmanPos != indexGhost and indexGhost not in ghostPos:
                indexGhost = (random.randint(1, length), random.randint(1, height))
        ghostPos.append(indexGhost)
    for r in range(length):
        line = ""
        for c in range(height):
            if (r, c) == pacmanPos:
                # print("P",end="")
                line += "P"
                continue
            if (r, c) in ghostPos:
                # print("G",end="")
                line += "G"
                continue
            if (r == 0 or r == length - 1) or (c == 0 or c == height - 1):
                # print("%", end="")
                line += "%"
            else:
                randomList = random.choices(itemsLayout, weights=(weights[0], weights[1], weights[2]))
                index = itemsLayout.index(randomList[0])
                if index == 0:
                    # print("o",end="")
                    line += "o"
                elif index == 1:
                    # print("%",end="")
                    line += "%"
                else:
                    # print(".",end="")
                    line += "."
        f.write(line + "\n")


def save_layout(layout, size, index):
    folder = f"layouts/{size}"
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/{size}_layout_{index}.lay"
    with open(filename, 'w') as f:
        for row in layout:
            f.write(''.join(row) + '\n')


sizes = {
    'small': (5, 10, 6, 12, 60, 80, 1, 2),
    'medium': (13, 20, 8, 15, 60, 80, 1, 3),
    'large': (15, 35, 10, 20, 60, 80, 1, 3)}

for size, params in sizes.items():
    print(f"Generating {size} layouts...")
    min_width, max_width, min_height, max_height, min_food, max_food, min_ghosts, max_ghosts = params
    weights = []
    if size == 'small':
        weights = [20, 60, 25]
    elif size == 'medium':
        weights = [5, 15, 100]
    else:
        weights = [5, 25, 100]
    for i in range(1, 36):
        generate_layout(min_width, max_width, min_height, max_height, min_food, max_food, min_ghosts,
                        max_ghosts, weights, size, i)
        print(f"Layout {i} generated for {size}.")

print("Layout generation completed.")
