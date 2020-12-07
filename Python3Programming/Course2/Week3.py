# 12.2. Function Definition
def hello():
    """This function says hello and greets you"""
    print("Hello")
    print("Glad to meet you")

# Assessment: Functions
# Q1
# Write a function called int_return that takes an integer as input and returns the same integer.

def int_return(i):
    return i

# Q2
# Write a function called add that takes any number as its input and returns that sum with 2 added.

def add(a):
    return a + 2

# Q3
# Write a function called change that takes any string, adds “Nice to meet you!” to the
# end of the argument given, and returns that new string.

def change(str):
    return str + "Nice to meet you!"

# Q4
# Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def accum(i):
    sum = 0
    for num in i:
        sum += num
    return sum

# Q5
# Write a function, length, that takes in a list as the input. If the length of the list is
# greater than or equal to 5, return “Longer than 5”.
# If the length is less than 5, return “Less than 5”.

def length(list):
    if len(list) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"

# Q6
# You will need to write two functions for this problem. The first function, divide that takes in
# any number and returns that same number divided by 2. The second function called sum should take
# any number, divide it by 2, and add 6. It should return this new number. You should call the divide
# function within the sum function. Do not worry about decimals.

def divide(num):
    return num / 2

def sum(num):
    return divide(num) + 6

# 13.2. Tuple Packing
# Wherever python expects a single value, if multiple expressions are provided, separated by commas,
# they are automatically packed into a tuple. For example, we can omit the parentheses when assigning
# a tuple of values to a single variable.

# julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# # or equivalently
# julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
# print(julia[4])

# 13.3. Tuple Assignment with Unpacking

# julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
#
# name, surname, birth_year, movie, movie_year, profession, birth_place = julia
#
# print(name, surname, birth_year, movie, movie_year, profession, birth_place)

# 13.5. Unpacking Tuples as Arguments to Function Calls
# def add(x, y):
#     return x + y
#
# print(add(3, 4))
# z = (5, 4)
# print(add(*z)) # this line will cause the values to be unpacked

# Assessment: Tuples

# Q1
# Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”.

# olympics = ('Beijing', 'London', 'Rio', 'Tokyo')

# Q2
# The list below, tuples_lst, is a list of tuples.
# Create a list of the second elements of each tuple and assign this list to the variable country.

# tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
# country = list()
#
# for tuple in tuples_lst:
#     country.append(tuple[1])
#
# print(country)

# Q3
# With only one line of code,
# assign the variables city, country, and year to the values of the tuple olymp.
# olymp = ('Rio', 'Brazil', 2016)
#
# city = olymp[0]
# country = olymp[1]
# year = olymp[2]

# Q4
# Define a function called info with five parameters: name, gender, age, bday_month, and hometown.
# The function should then return a tuple with all five parameters in that order.

# def info(name, gender, age, bday_month, hometown):
#     return (name, gender, age, bday_month, hometown)

# Q5
# Given is the dictionary, gold, which shows the country and the number of gold medals they have
# earned so far in the 2016 Olympics. Create a list, num_medals, that contains only the number of
# medals for each country. You must use the .items() method. Note: The .items() method provides a
# list of tuples. Do not use .keys() method.

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}

num_medals = list()
print(gold.items())

for tuple in gold.items():
    num_medals.append(tuple[1])