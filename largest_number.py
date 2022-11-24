numbers = [2, 7, 8, 22, 14, 78, 99, 13, 6]
# largest_num = 0
largest_num = numbers[0]

for number in numbers:
    if number > largest_num:
        largest_num = number
print(largest_num)
