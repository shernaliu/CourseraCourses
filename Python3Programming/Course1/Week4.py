# Mutability
# fruit = ["banana", "apple", "cherry"]
# print(fruit)
#
# fruit[0] = "pear"
# fruit[-1] = "orange" #wow
# print(fruit)

# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# alist[1:3] = ['x', 'y']
# print(alist)

# same as deleting
# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# alist[1:3] = []
# print(alist)

# greeting = "Hello, world!"
# newGreeting = 'J' + greeting[1:]
# print(newGreeting)
# print(greeting)
#
# phrase = "many moons"
# phrase_expanded = phrase + " and many stars"
# phrase_larger = phrase_expanded + " litter"
# phrase_complete = "M" + phrase_larger[1:] + " the night sky."
# excited_phrase_complete = phrase_complete[:-1] + "!"
# print(excited_phrase_complete)

# List Element Deletion
# a = ['one', 'two', 'three']
# del a[1]
# print(a)
#
# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# del alist[1:5]
# print(alist)

# Cloning lists
# a = [81,82,83]
# b = a[:] # make a clone using splice
# print(a == b)
# print(a is b)
#
# b[0] = 5
# print(a)
# print(b)

# Week 4 Assignment 1
# Q1
# b = ['q', 'u', 'i']
# z = b
# b[1] = 'i'
# z.remove('i')
# print(z)

# Q2
# sent = "Holidays can be a fun time when you have good company!"
# phrase = sent
# phrase = phrase + " Holidays can also be fun on your own!"
# print(phrase)

# Q3
# lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
# lst.remove('pluto')
# first_three = lst[:3]
# print(lst)
# print(first_three)

# Q4
# x = ["dogs", "cats", "birds", "reptiles"]
# y = x
# x += ['fish', 'horses']
# y = y + ['sheep']
# print(x)
# print(y)

# Q5
# sent = "The mall has excellent sales right now."
# wrds = sent.split()
# wrds[1] = 'store'
# new_sent = " ".join(wrds) # changes to a string by joining each element with space in between
# print(sent)
# print(wrds)
# print(new_sent)

# Methods on Lists
# mylist = []
# mylist.append(5)
# mylist.append(27)
# mylist.append(3)
# mylist.append(12)
# print(mylist)
#
# mylist.insert(1, 12) # insert value 12 at position 1
# print(mylist)
# print(mylist.count(12)) # count how many 12 are inside the list
#
# print(mylist.index(3)) # give element at index 3
# print(mylist.count(5)) # count how many 5 are inside the list
#
# mylist.reverse()
# print(mylist)
#
# mylist.sort()
# print(mylist) # sort ascending order
#
# mylist.remove(5) # remove 5 from the list
# print(mylist)
#
# lastitem = mylist.pop() # removes and returns the last elemetn of the list
# print("pop:",lastitem)
# print(mylist)

# Week 4 Assignment 2

# Q1
# sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
#
# sports.insert(2, "horseback riding")
# print(sports)

# Q2
# trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
#
# trav_dest.remove("London")
# print(trav_dest)

# Q3
# trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
#
# trav_dest.append("Guadalajara")
# print(trav_dest)

# Q4
# winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
# winners.sort()
# print(winners)

# Q5
# winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
#
# z_winners = list()
# winners.sort()
# winners.reverse()
# for winner in winners:
#     z_winners.append(winner)
#
# print(z_winners)

# Week 4 Assignment 3
# Q1
# str1 = "I love python"
# # HINT: what's the accumulator? That should go here.
# chars = list()
# for char in str1:
#     chars.append(char)
#
# print(chars)

# Week 4 Assignment 4
# Q1
# lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
# lst.remove('pluto')
# first_three = lst[:3]
# print(lst)
# print(first_three)

# Q2
# a = ["holiday", "celebrate!"]
# quiet = a
# quiet.append("company")
# print(a)

# Q3
# ael = "python!"
# app = list()
# for letter in ael:
#     app.append(letter)
#
# print(app)

# Q4
# wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
# past_wrds = list()
#
# for word in wrds:
#     past_wrds.append(word+"ed")
#
# print(past_wrds)

# Assignment: Final Course Assignment
# Q1
# scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
# a_scores = 0
#
# scores_list = scores.split(" ")
# for score in scores_list:
#     if int(score) >= 90:
#         a_scores += 1
# print(a_scores)

# Q2
# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
# org = "The organization for health, safety, and education"
# acro = ""
#
# # split org
# org_list = org.split(" ")
#
# for bad_word in stopwords:
#     if bad_word in org_list:
#         org_list.remove(bad_word)
#
# print(org_list)
#
# for word in org_list:
#     acro += word[0:1].upper()
#
# print(acro)

# Q3
# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
# sent = "The water earth and air are vital"
# acro = ""
#
# # split
# sent_list = sent.split(" ")
#
# for bad_word in stopwords:
#     if bad_word in sent_list:
#         sent_list.remove(bad_word)
#
# print(sent_list)
#
# last_word = sent_list[len(sent_list)-1]
# print(last_word)
#
# for word in sent_list:
#     if not last_word is word: # if its not the last word, append . space at the end
#         acro += word[0:2].upper() + ". "
#     else:
#         acro += word[0:2].upper() # it is the last word, dont need append . space at the end
#
# print(acro)

# Q4
# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
# p_phrase = "was it a car or a cat I saw"
# r_phrase  = ""
#
# if p_phrase == p_phrase[::-1]:
#     print("Its palindrome")
# else:
#     print("Its not palindrome")
#
# r_phrase = p_phrase[::-1]
# print(r_phrase)

# Q5
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    item_list = item.split(", ")
    print("The store has {} {}, each for {} USD.".format(item_list[1], item_list[0], item_list[2]))


