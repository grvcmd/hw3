# Lab 11.22

"""Write a program that reads a list of words. Then, the program
    outputs those words and their frequencies."""

user_input = input()

word_list = user_input.split()

for word in word_list:
    frequency = word_list.count(word)

    print('{} {}'.format(word, frequency))