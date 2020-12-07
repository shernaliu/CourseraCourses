# Assessment: More about Iteration

# Q1
# Write a function, sublist, that takes in a list of numbers as the parameter.
# In the function, use a while loop to return a sublist of the input list.
# The sublist should contain the same values of the original list up until it
# reaches the number 5 (it should not contain the number 5).

# def sublist(numList):
#     slist = list()
#     for num in numList:
#         if num == 5:
#             break
#         slist.append(num)
#     return slist

# Q2
# Write a function called check_nums that takes a list as its parameter,
# and contains a while loop that only stops once the element of the list is
# the number 7. What is returned is a list of all of the numbers up until it
# reaches 7.

# def check_nums(lst):
#     nlist = list()
#     for num in lst:
#         if num == 7:
#             break
#         nlist.append(num)
#     return nlist

# Q3
# Write a function, sublist, that takes in a list of strings as the parameter.
# In the function, use a while loop to return a sublist of the input list.
# The sublist should contain the same values of the original list up until
# it reaches the string “STOP” (it should not contain the string “STOP”).

# def sublist(strList):
#     slist = list()
#     for str in strList:
#         if str == "STOP":
#             break
#         slist.append(str)
#     return slist

# Q4
# Write a function called stop_at_z that iterates through a list of strings.
# Using a while loop, append each string to a new list until the string that
# appears is “z”. The function should return the new list.

# def stop_at_z(strList):
#     newList = list()
#     for str in strList:
#         if str == "z":
#             break
#         newList.append(str)
#     return newList

# Q5
# Below is a for loop that works. Underneath the for loop, rewrite the problem
# so that it does the same thing, but using a while loop instead of a for loop.
# Assign the accumulated total in the while loop code to the variable sum2.
# Once complete, sum2 should equal sum1.

# sum1 = 0
#
# lst = [65, 78, 21, 33]
#
# for x in lst:
#     sum1 = sum1 + x
#
#
# sum2 = 0
# i = 0
# while i < len(lst):
#     sum2 += lst[i]
#     i += 1
#
# print(sum2)

# Q6
# Challenge: Write a function called beginning that takes a list as input and
# contains a while loop that only stops once the element of the list is the
# string ‘bye’. What is returned is a list that contains up to the first 10
# strings, regardless of where the loop stops. (i.e., if it stops on the 32nd
# element, the first 10 are returned. If “bye” is the 5th element, the first 4
# are returned.) If you want to make this even more of a challenge, do this
# without slicing

# def beginning(lst):
#
#     # init counter
#     counter = 0
#     sublist = list()
#
#     for str in lst:
#         if counter == 10:
#             return sublist
#         elif str == "bye":
#             return sublist
#         else:
#             sublist.append(str)
#         counter += 1
#
# test1 = beginning(['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat', 'facebook', 'social media'])
# print(test1)
#
# test2 = beginning(['bye', 'no', 'yes', 'maybe', 'sorta'])
# print(test2)
#
# test3 = beginning(['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night'])
# print(test3)

# 15.1. Introduction: Optional Parameters
# print(int("100"))
# print(int("100", 10))   # same thing, 10 is the default value for the base
# print(int("100", 8))     # now the base is 8, so the result is 1*64 = 64

# 15.2. Keyword Parameters
# initial = 7
# def f(x, y=3, z=initial):
#     print("x, y, z, are: " + str(x) + " " + str(y) + " " + str(z) )
#
# f(2)
# f(2, z=8)

# names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
# for name, scores in names_scores:
#     print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))


# # this works
# names = ["Jack","Jill","Mary"]
# for n in names:
#     print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))
#
# # but this also works!
# names = ["Jack","Jill","Mary"]
# for n in names:
#     print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))

# Anonymous Function with Lambda Expressions
# ALternative way of writing functions

# def f(x):
#     return x - 1
#
# print(f)
# print(type(f))
# print(f(3))
#
# print(lambda x: x-2)
# print(type(lambda x: x-2))
# print((lambda x: x-2)(6))
#
# def last_char(s):
#     return s[-1]
#
# last_char = lambda s: s[-1]

# Assessment: Advanced Functions
# Q1
# Create a function called mult that has two parameters, the first is required and should be an
# integer, the second is an optional parameter that can either be a number or a string but whose
# default is 6. The function should return the first parameter multiplied by the second.

# def mult(i, x = 6):
#     return i * x
#
#
# print(mult(2))
# print(mult(3,5))
# print(mult(4,'hello'))

# Q2
# The following function, greeting, does not work. Please fix the code so that it runs without error.
# This only requires one change in the definition of the function.

# def greeting(name, greeting="Hello ", excl="!"):
#     return greeting + name + excl
#
# print(greeting("Bob"))
# print(greeting(""))
# print(greeting("Bob", excl="!!!"))

# Q3
# Below is a function, sum, that does not work. Change the function definition so the code works.
# The function should still have a required parameter, intx, and an optional parameter,
# intz with a defualt value of 5.

def sum(intx,intz=5):
    return intz + intx

# Q4
# Write a function, test, that takes in three parameters: a required integer, an optional boolean
# whose default value is True, and an optional dictionary, called dict1, whose default value is
# {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the
# integer is a key in the dictionary. The value of that key should then be returned.
# If the boolean parameter is False, return the boolean value “False”.

# def test(i, boo=True, dict1={2:3, 4:5, 6:8}):
#     if boo == True:
#         for key in dict1.keys():
#             if key == i:
#                 return dict1[key]
#     else:
#         return False
#
# print(test(2))
# print(test(4,False))
# print(test(5,dict1={5:4, 2:1}))


# Q5

def checkingIfIn(str, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        for key in d.keys():
            if key == str:
                return True
        return False
    else:
        for key in d.keys():
            if key == str:
                return False
        return True

# Q6


def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn("cherry")
print(c_false)

# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn("cherry", False)
print(c_true)

# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn("fruit")
print(fruit_ans)

# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn("fruit", d = {'apple': 2, 'pear': 1, 'fruit': 8, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7})
print(param_check)
