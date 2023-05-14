vowels = 0
consonants = 0
vowels_list = ['a','e','i','o','u','y']
lines_num = int(input('How many lines will there be?'))

for _ in range(lines_num):
    line = input()
    for char in line:
        if char.lower() in vowels_list:
            vowels += 1
        elif char.lower().isalpha():
            consonants += 1


print("Number of vowels:" + str(vowels))
print("Number of vowels:" + str(consonants))
