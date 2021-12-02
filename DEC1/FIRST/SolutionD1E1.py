numbers = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        try:
            numbers.append(int(line[:-1]))
        except ValueError:
            print(f"Invalid number string '{line[:-1]}'")

increases = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        increases += 1

print(f"Number of increases: {increases}")
