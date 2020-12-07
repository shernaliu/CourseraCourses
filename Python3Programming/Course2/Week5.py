# 16.1. Introduction: Sorting with Sort and Sorted
# L1 = [1, 7, 4, -2, 3]
# L2 = ["Cherry", "Apple", "Blueberry"]
#
# L1.sort()
# print(L1)
# L2.sort()
# print(L2)

# V2

# L2 = ["Cherry", "Apple", "Blueberry"]
#
# L3 = sorted(L2)
# print(L3)
# print(sorted(L2))
# print(L2) # unchanged
#
# print("----")
#
# L2.sort()
# print(L2)
# print(L2.sort())  #return value is None

# 16.2. Optional reverse parameter
# L2 = ["Cherry", "Apple", "Blueberry"]
# print(sorted(L2, reverse=True))

# 16.3. Optional key parameter
# v1
# L1 = [1, 7, 4, -2, 3]

# def absolute(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print(absolute(3))
# print(absolute(-119))
#
# for y in L1:
#     print(absolute(y))

# v2
# L1 = [1, 7, 4, -2, 3]
#
# def absolute(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# L2 = sorted(L1, key=absolute)
# print(L2)
#
# #or in reverse order
# print(sorted(L1, reverse=True, key=absolute))

# v3
# L1 = [1, 7, 4, -2, 3]
#
# def absolute(x):
#     print("--- figuring out what to write on the post-it note for " + str(x))
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print("About to call sorted")
# L2 = sorted(L1, key=absolute)
# print("Finished execution of sorted")
# print(L2)

# 16.4. Sorting a Dictionary
# For example, the following code counts the frequencies of different numbers in the list.
# L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
#
# d = {}
# for x in L:
#     if x in d:
#         d[x] = d[x] + 1
#     else:
#         d[x] = 1
# for x in d.keys():
#     print("{} appears {} times".format(x, d[x]))


# Sorting the keys in alphabetical order
# L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
#
# d = {}
# for x in L:
#     if x in d:
#         d[x] = d[x] + 1
#     else:
#         d[x] = 1
# y = sorted(d.keys())
# for k in y:
#     print("{} appears {} times".format(k, d[k]))

# Sorting the keys in key's value in desc order using lambda
# L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
#
# d = {}
# for x in L:
#     if x in d:
#         d[x] = d[x] + 1
#     else:
#         d[x] = 1
#
# y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
# for k in y:
#     print("{} appears {} times".format(k, d[k]))

# V2 of previous using a named function.
# L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
#
# d = {}
# for x in L:
#     if x in d:
#         d[x] = d[x] + 1
#     else:
#         d[x] = 1
#
# def g(k):
#     return d[k]
#
# y =(sorted(d.keys(), key=g, reverse=True))
#
# # now loop through the keys
# for k in y:
#     print("{} appears {} times".format(k, d[k]))


# V3
# L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
#
# d = {}
# for x in L:
#     if x in d:
#         d[x] = d[x] + 1
#     else:
#         d[x] = 1
#
# # now loop through the sorted keys
# for k in sorted(d, key=lambda k: d[k], reverse=True):
#       print("{} appears {} times".format(k, d[k]))

# 16.5. Breaking Ties: Second Sorting
# V1 - Sort by tuple. Look at first element, second element, third element.
# tups = [('A', 3, 2),
#         ('C', 1, 4),
#         ('B', 3, 1),
#         ('A', 2, 4),
#         ('C', 1, 2)]
# for tup in sorted(tups):
#     print(tup)

# V2 - sort a list of fruit words first by their length, smallest to largest, and then
# alphabetically to break ties among words of the same length
# fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
# new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
# for fruit in new_order:
#     print(fruit)

# V3 - sort it by largest to smallest, and then by alphabetical order?
# fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
# new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name), reverse=True)
# for fruit in new_order:
#     print(fruit)

# Do you see a problem here? Not only does it sort the words from largest to smallest,
# but also in reverse alphabetical order! Can you think of any ways you can solve this issue?

# One solution is to add a negative sign in front of len(fruit_name), which will convert all positive
# numbers to negative, and all negative numbers to positive. As a result, the longest elements
# would be first and the shortest elements would be last.

# fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
# new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
# for fruit in new_order:
#     print(fruit)


# 16.6 When to use a Lambda Expression
# V1 - Sort by the length of the city of each state in US
# states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
#           "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
#           "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}
#
# print(sorted(states, key=lambda state: len(states[state][0])))

# Assessment: Sorting

# Q1
# Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.

# letters = "alwnfiwaksuezlaeiajsdl"
# sorted_letters = ""
# sorted_letters = sorted(letters, reverse=True)
# print(sorted_letters)

# Q2
# Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.

# animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
# animals_sorted = sorted(animals)
# print(animals_sorted)

# Q3
# The dictionary, medals, shows the medal count for six countries during the Rio Olympics.
# Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.

# medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
# alphabetical = sorted(medals)
# print(alphabetical)

# Q4
# Given the same dictionary, medals, now sort by the medal count.
# Save the three countries with the highest medal count to the list, top_three.

# medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
#
# sorted_medal_count = sorted(medals, key = lambda country: medals[country], reverse=True)
# print(sorted_medal_count)
#
# top_three = sorted_medal_count[:3]
# print(top_three)

# Q5
# We have provided the dictionary groceries. You should return a list of its keys, but they should be
# sorted by their values, from highest to lowest. Save the new list as most_needed.

# groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
#
# most_needed = sorted(groceries, key = lambda item:groceries[item], reverse=True)
# print(most_needed)

# Q6
# Create a function called last_four that takes in an ID number and returns the last four digits.
# For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids
# stored in the variable, ids, from lowest to highest. Save this sorted list in the variable,
# sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.

# def last_four(x):
#     return str(x)[len(str(x))-4:]
#
# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
# sorted_ids = sorted(ids, key = last_four)
# print(sorted_ids)

# Q7
# Sort the list ids by the last four digits of each id.
# Do this using lambda and not using a defined function.
# Save this sorted list in the variable sorted_id.

# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
# sorted_id = sorted(ids, key = lambda x : str(x)[len(str(x))-4:])
# print(sorted_id)

# Q8
# Sort the following list by each element’s second letter a to z.
# Do so by using lambda. Assign the resulting value to the variable lambda_sort.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key = lambda char : char[1])
print(lambda_sort)



