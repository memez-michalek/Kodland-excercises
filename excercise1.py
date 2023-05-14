integer_list = [4, 0, 5, 0, 3, 0, 0, 5 ]

left = 0
right = len(integer_list) - 1

while left < right:
    if integer_list[left] == 0 and integer_list[right] != 0:
        integer_list[left], integer_list[right] = integer_list[right], integer_list[left]
    if integer_list[left] != 0:
        left += 1
    if integer_list[right] == 0:
        right -= 1

print(integer_list)