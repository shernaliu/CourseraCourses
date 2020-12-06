# Week3 Assignment 1
# Q1
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

rainfall_mi_list_float = list()
num_rainy_months = 0

# split to list of strings
rainfall_mi_list_str = rainfall_mi.split(", ")

for str in rainfall_mi_list_str:
    rainfall_mi_list_float.append(float(str))

for value in rainfall_mi_list_float:
    if value > 3:
        num_rainy_months += 1

# Q2
# sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
#
# # Write your code here.
# same_letter_count = 0
#
# # split to list of strings
# sentence_list = sentence.split(" ")
#
# for word in sentence_list:
#     # increment count if length of word is 1 (satisfy condition that it end and start with same letter)
#     if len(word) == 1:
#         same_letter_count += 1
#     # check first letter and last letter of the word using slicing
#     elif word[0:1] == word[len(word)-1:]:
#         same_letter_count += 1
#
# print(same_letter_count)

# Q3
# items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
#
# acc_num = 0
# for word in items:
#     if "w" in word:
#         acc_num += 1
#
# print(acc_num)

# Q4
# sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
#
# num_a_or_e = 0
# list = sentence.split(" ")
# for word in list:
#     if "a" in word or "e" in word:
#         num_a_or_e += 1
#
# print(num_a_or_e)

# Q5
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.
num_vowels = 0
list = s.split(" ")
for word in list:
    for letter in word:
        if letter in vowels:
            num_vowels += 1

print(num_vowels)