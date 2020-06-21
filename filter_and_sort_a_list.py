# Lab 11.18

""" Program that gets a list of integers from input, and
    outputs non-negative integers from least to greatest """

user_input = input().split()

positive_numbers = []

for num in user_input:
    num = int(num) # converts string number into integer

    if num >= 0:
        positive_numbers.append(num)

positive_numbers.sort() # sorts list from least to greatest

# print list like >>> 2 4 7 20
for i in positive_numbers:
    print(i, end='')


