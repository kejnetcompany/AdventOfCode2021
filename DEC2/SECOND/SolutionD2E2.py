instructions = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        elements = line[:-1].split(" ")
        instructions.append((elements[0], int(elements[1])))

position = 0
depth = 0
aim = 0

for instruction in instructions:
    if instruction[0] == "forward":
        position += instruction[1]
        depth += aim * instruction[1]
    if instruction[0] == "down":
        aim += instruction[1]
    if instruction[0] == "up":
        aim -= instruction[1]

print(f"Answer: {position * depth}")
