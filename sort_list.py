numbers = [10, 22, 34, 67, 69, 55, 44, 33, 22, 34, 20, 10, 69, 34]
new_numbers = []

for number in numbers:
    if number not in new_numbers:
        new_numbers.append(number)
print(new_numbers)

#     if numbers.count(number) > 1:
#         numbers.remove(number)
#         new_numbers = numbers.copy()
#     # else:
#     #     new_numbers.append(number)
# print(new_numbers)
