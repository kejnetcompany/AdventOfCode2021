numbers = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        try:
            numbers.append(int(line[:-1]))
        except ValueError:
            print(f"Invalid number string '{line[:-1]}'")

window_size = 3
window_increases = 0
for i in range(3, len(numbers)):
    previous_window_sum = sum(numbers[i - 1 - (window_size - 1): i])
    current_window_sum = sum(numbers[i - (window_size - 1): i+1])
    if current_window_sum > previous_window_sum:
        window_increases += 1

print(f"Number of window increases with window size {window_size}: {window_increases}")
