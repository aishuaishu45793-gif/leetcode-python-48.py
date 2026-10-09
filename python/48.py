# 115. Move Negative Numbers to the Beginning

numbers = [3, -1, 5, -7, 2, -4, 8]

negative = []
non_negative = []

for number in numbers:
    if number < 0:
        negative.append(number)
    else:
        non_negative.append(number)

result = negative + non_negative

print("Result:", result)