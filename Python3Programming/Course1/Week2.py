# Week 2 Assignment 1
# Q1
# let = "z"
# let_two = "p"
# c = let_two + let
# m = c*5
# print(m)

# Q2
# sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
# last = sports[len(sports)-3:]
# print(last)

# Q3
# by = "You are"
# az = "doing a great "
# io = "job"
# qy = "keep it up!"
#
# message = by + " " + az + io + ", " + qy
# print(message)

# Q4
# ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
# new = ls[2:4]
# print(new)

# Q5
# l = ['w', '7', 0, 9]
# m = l[1:2]
# print(type(m))

# Q6
# l = ['w', '7', 0, 9]
# m = l[1]
# print(type(m))

# Q7
# b = "My, what a lovely day"
# x = b.split(',')
# print(type(x))

# Q8
# b = "My, what a lovely day"
# x = b.split(',')
# z = "".join(x)
# y = z.split()
# a = "".join(y)
# print(type(a))

# Week 2 Assignment 2
# Q1
# my_str = "MICHIGAN"
# for letter in my_str:
#     print(letter)

# Q2
# several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
#
# for item in several_things:
#     print(item)
#
# for item in several_things:
#     print(type(item))

# Q3
# str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
#
# # Write your code here.
# for item in str_list:
#     print(len(item))


# Q4
# original_str = "The quick brown rhino jumped over the extremely lazy fox."
#
# num_chars = 0
#
# for letter in original_str:
#     num_chars += 1
#
# print(num_chars)

# Q5
# addition_str = "2+5+10+20"
#
# sum_val = 0
# list = addition_str.split("+")
# for num in list:
#     sum_val += int(num)

# Q6
# week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
#
# sum_temp = 0
# avg_temp = 0
# templist = week_temps_f.split(",")
#
# # sum up all the temps
# for temp in templist:
#     sum_temp += float(temp)
#
# # calculate average
# avg_temp = sum_temp / len(templist)

# Q7
# nums = list()
# for i in range(68):
#     nums.append(i)
# print(nums)

# Q8
# original_str = "The quick brown rhino jumped over the extremely lazy fox"
# num_words_list = list()
#
# stringlist = original_str.split(" ")
# print(stringlist)
# print(len(stringlist))
#
# for word in stringlist:
#     num_words_list.append(len(word))
#
# print(num_words_list)

# Q9
# lett = ""
#
# for i in range(7):
#     lett += "b"
# print(lett)