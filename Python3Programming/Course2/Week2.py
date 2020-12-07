# 11.2. Getting Started with Dictionaries
# eng2sp = {}
# eng2sp['one'] = 'uno'
# eng2sp['two'] = 'dos'
# eng2sp['three'] = 'tres'
# print(eng2sp)

# eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
# print(eng2sp)

# mydict = {"cat":12, "dog":6, "elephant":23}
# print(mydict["dog"])

# inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

# del inventory['pears']
# print(inventory)

# inventory['pears'] = 0
# print(inventory)

# inventory['bananas'] = inventory['bananas'] + 200
# print(inventory)

# 11.4. Dictionary methods
# inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
#
# for akey in inventory.keys():     # the order in which we get the keys is not defined
#     print("Got key", akey, "which maps to value", inventory[akey])
#
# ks = list(inventory.keys())
# print(ks)
#
# print(list(inventory.values()))
# print(list(inventory.items()))
#
# if 'bananas' in inventory:
#     print("We have {} bananas".format(inventory['bananas']))
# else:
#     print("We have no bananas")
#
# print(inventory.get('cherries')) # None
# print('cherries' in inventory) # False

# 11.5. Aliasing and copying

# opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
# alias = opposites
#
# print(alias is opposites) # Are they pointing to the same object? True.
#
# alias['right'] = 'left'
# print(opposites['right'])
# print(alias)
# print(opposites)

# Assessment: Dictionary Mechanics

# Q1
# At the halfway point during the Rio Olympics,
# the United States had 70 medals, Great Britain had 38 medals,
# China had 45 medals, Russia had 30 medals, and Germany had 17 medals.
# Create a dictionary assigned to the variable medal_count with the country names as the keys
# and the number of medals the country had as each key’s value.

# medal_count = {'United States': 70, 'Great Britain': 38, 'China': 45, 'Russia': 30, 'Germany': 17}

# Q2
# Given the dictionary swimmers, add an additional key-value pair to
# the dictionary with "Phelps" as the key and the integer 23 as the value.
# Do not rewrite the entire dictionary.

# swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}
# swimmers.update({'Phelps': 23})
# print(swimmers)

# Q3
# Add the string “hockey” as a key to the dictionary sports_periods and assign it the value of 3.
# Do not rewrite the entire dictionary.

# sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}
# sports_periods.update({'hockey': 3})

# Q4
# The dictionary golds contains information about how many gold medals each country
# won in the 2016 Olympics. But today, Spain won 2 more gold medals.
# Update golds to reflect this information.

# golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
# golds['Spain'] = golds['Spain'] + 2

# Q5
#  Create a list of the countries that are in the dictionary golds,
#  and assign that list to the variable name countries. Do not hard code this.
# golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
# countries = list(golds.keys())
# print(countries)

# Q6
# Provided is the dictionary, medal_count, which lists countries and their respective medal count
# at the halfway point in the 2016 Rio Olympics. Using dictionary mechanics,
# assign the medal count value for "Belarus" to the variable belarus. Do not hardcode this.
# medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}
# belarus = medal_count['Belarus']

# Q7
# The dictionary total_golds contains the total number of gold medals that countries
# have won over the course of history. Use dictionary mechanics to find the number of golds
# Chile has won, and assign that number to the variable name chile_golds. Do not hard code this!
# total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111, "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87, "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22, "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209, "Uganda": 7,  "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}
# chile_golds = total_golds['Chile']

# Q8
# Provided is a dictionary called US_medals which has the first 70 metals that the United States
# has won in 2016, and in which category they have won it in. Using dictionary mechanics,
# assign the value of the key "Fencing" to a variable fencing_value. Remember, do not hard code this.
# US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2, "Golf": 1, "Weightlifting": 1}
# fencing_value = US_medals['Fencing']

# 11.6. Introduction: Accumulating Multiple Results In a Dictionary
# If we want to find out how often the letter ‘t’ occurs, we can accumulate the result in a count variable.
# f = open('scarlet.txt', 'r')
# txt = f.read()
# # now txt is one long string containing all the characters
# t_count = 0 #initialize the accumulator variable
# for c in txt:
#     if c == 't':
#         t_count = t_count + 1   #increment the counter
# print("t: " + str(t_count) + " occurrences")

# We can accumulate counts for more than one character as we traverse the text.
# Suppose, for example, we wanted to compare the counts of ‘t’ and ‘s’ in the text.
# f = open('scarlet.txt', 'r')
# txt = f.read()
# # now txt is one long string containing all the characters
# t_count = 0 #initialize the accumulator variable
# s_count = 0 # initialize the s counter accumulator as well
# for c in txt:
#     if c == 't':
#         t_count = t_count + 1   #increment the t counter
#     elif c == 's':
#         s_count = s_count + 1
# print("t: " + str(t_count) + " occurrences")
# print("s: " + str(s_count) + " occurrences")

# One dictionary can hold all of the accumulator variables.
# Each key in the dictionary will be one letter, and the corresponding value will be the count so far
# of how many times that letter has occurred.
# f = open('scarlet.txt', 'r')
# txt = f.read()
# # now txt is one long string containing all the characters
# x = {} # start with an empty dictionary
# x['t'] = 0  # initialize the t counter
# x['s'] = 0  # initialize the s counter
# for c in txt:
#     if c == 't':
#         x['t'] = x['t'] + 1  # increment the t counter
#     elif c == 's':
#         x['s'] = x['s'] + 1  # increment the s counter
#
# print("t: " + str(x['t']) + " occurrences")
# print("s: " + str(x['s']) + " occurrences")


# Final version is best version.
# Rather than pre-specifying which letters to keep accumulator counts for,
# we can start with an empty dictionary and add a counter to the dictionary each time
# we encounter a new thing that we want to start keeping count of.

# f = open('scarlet.txt', 'r')
# txt = f.read()
# # now txt is one long string containing all the characters
# x = {} # start with an empty dictionary
# for c in txt:
#     if c not in x:
#         # we have not seen this character before, so initialize a counter for it
#         x[c] = 0
#
#     #whether we've seen it before or not, increment its counter
#     x[c] = x[c] + 1
#
# print("t: " + str(x['t']) + " occurrences")
# print("s: " + str(x['s']) + " occurrences")
# for c in x.keys():
#     print(c + ": " + str(x[c]) + " occurrences")

#  Assessment: Dictionary Accumulation

# Q1
# The dictionary Junior shows a schedule for a junior year semester.
# The key is the course name and the value is the number of credits.
# Find the total number of credits taken this semester and assign it to the variable credits.
# Do not hardcode this – use dictionary accumulation!

# Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
# credits = 0
# for key in Junior:
#     credits = credits + Junior[key]
#
# print(credits)

# Q2
# Create a dictionary, freq, that displays each character in string str1 as the key and
# its frequency as the value.

# str1 = "peter piper picked a peck of pickled peppers"
#
# freq= {}
#
# for char in str1:
#     if char not in freq:
#         # we have not seen this character before, so initialize a counter for it
#         freq[char] = 0
#
#     #whether we've seen it before or not, increment its counter
#     freq[char] = freq[char] + 1
#
# for char in freq.keys():
#     print(char + ": " + str(freq[char]) + " occurrences")

# Q3
# Provided is a string saved to the variable name s1.
# Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.

# s1 = "hello"
# counts = {}
#
# for char in s1:
#     if char not in counts:
#         # we have not seen this character before, so initialize a counter for it
#         counts[char] = 0
#
#     #whether we've seen it before or not, increment its counter
#     counts[char] = counts[char] + 1
#
# for char in counts.keys():
#     print(char + ": " + str(counts[char]) + " occurrences")

# Q4
# Create a dictionary, freq_words,
# that contains each word in string str1 as the key and its frequency as the value.

# str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
# freq_words = {}
# list = str1.split()
# for word in list:
#     if word not in freq_words:
#         freq_words[word] = 0
#     freq_words[word] += 1
#
# for char in freq_words.keys():
#     print(char + ": " + str(freq_words[char]) + " occurrences")

# Q5
# Create a dictionary called wrd_d from the string sent,
# so that the key is a word and the value is how many times you have seen that word.

# sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
# wrd_d = {}
# list = sent.split()
# for word in list:
#     if word not in wrd_d:
#         wrd_d[word] = 0
#     wrd_d[word] += 1
#
# for char in wrd_d.keys():
#     print(char + ": " + str(wrd_d[char]) + " occurrences")

# Q6
# Create the dictionary characters that shows each character from the string sally and its frequency.
# Then, find the most frequent letter based on the dictionary.
# Assign this letter to the variable best_char.

# sally = "sally sells sea shells by the sea shore"
# characters = {}
# for char in sally:
#     if char not in characters:
#         characters[char] = 0
#     characters[char] += 1
#
# best_char = ""
# highest = 0
#
# for char in characters.keys():
#     print(char + ": " + str(characters[char]) + " occurrences")
#     if characters[char] > highest:
#         best_char = char
#         highest = characters[char]
#
# print(best_char, "with", highest, "counts")

# Q7
# Find the least frequent letter. Create the dictionary characters that shows each character
# from string sally and its frequency. Then, find the least frequent letter in the string and
# assign the letter to the variable worst_char.

# sally = "sally sells sea shells by the sea shore and by the road"
# characters = {}
# for char in sally:
#     if char not in characters:
#         characters[char] = 0
#     characters[char] += 1
#
# worst_char = ""
# lowest = characters[sally[0:1]] # set first value as lowest for comparison
#
# for char in characters.keys():
#     print(char + ": " + str(characters[char]) + " occurrences")
#     if characters[char] < lowest:
#         worst_char = char
#         lowest = characters[char]
#
# print(worst_char, "with", lowest, "counts")

# Q8
# Create a dictionary named letter_counts that contains each letter and the number of times it occurs
# in string1. Challenge: Letters should not be counted separately as upper-case and lower-case.
# Intead, all of them should be counted as lower-case.
# string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
# letter_counts = {}
#
# for char in string1:
#     if char.lower() not in letter_counts:
#         letter_counts[char.lower()] = 0
#     letter_counts[char.lower()] += 1
#
# for char in letter_counts.keys():
#     print(char + ": " + str(letter_counts[char]) + " occurrences")

# Q9
# Create a dictionary called low_d that keeps track of all the characters in the string p
# and notes how many times each character was seen.
# Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen
# as a “t” for example.

# p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
# low_d = {}
#
# for char in p:
#     if char.lower() not in low_d:
#         low_d[char.lower()] = 0
#     low_d[char.lower()] += 1
#
# for char in low_d.keys():
#     print(char + ": " + str(low_d[char]) + " occurrences")
