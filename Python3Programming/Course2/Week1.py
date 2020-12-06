# 10.2. Reading a File
# fileref = open("olympics.txt", "r")

# contents = fileref.read() # read the entire contents of the file as 1 string
# print(contents[:100])
# print(len(contents))

# lines = fileref.readlines() # read as a list of strings
#print(lines[:4])

# for line in lines[:4]:
#     print(line.rstrip())

# shorter ver. to iterate thru each line
# file iteration supports iteration but not slices. aka cant use slice here.
# for line in fileref:
#     print(line.strip())

# fileref.close()

# 10.8. Writing Text Files
# fileObj = open("squares.txt", "w")
# for number in range(1, 13):
#     square = number * number
#     fileObj.write(str(square) + '\n')
# fileObj.close()
#
# newFileObj = open("squares.txt", "r")
# print(newFileObj.read()[:14]) # print first 14 chars (\n inclusive)

# 10.6. Using with for Files
# no need to .close() as it is executed automatically within the with code block
# with open('squares.txt', 'r') as md:
#     for line in md:
#         print(line)
# # continue on with other code

# 10.10. Reading in data from a CSV File
# fileconnection = open("olympics.txt", 'r')
# lines = fileconnection.readlines()
# header = lines[0]
# field_names = header.strip().split(',')
# print(field_names)
# for row in lines[1:]:
#     vals = row.strip().split(',')
#     if vals[5] != "NA":
#         print("{}: {}; {}".format(
#             vals[0],
#             vals[4],
#             vals[5]))
# fileconnection.close()

# 10.11. Writing data to a CSV File
# olympians = [("John Aalberg", 31, "Cross Country Skiing"),
#              ("Minna Maarit Aalto", 30, "Sailing"),
#              ("Win Valdemar Aaltonen", 54, "Art Competitions"),
#              ("Wakako Abe", 18, "Cycling")]
#
# outfile = open("reduced_olympics.csv", "w")
# # output the header row
# outfile.write('Name,Age,Sport')
# outfile.write('\n')
# # output each of the rows:
# for olympian in olympians:
#     row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
#     outfile.write(row_string)
#     outfile.write('\n')
# outfile.close()

### Assessment: Files and CSV
# Q1
# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
# # Find the total number of characters in the file and save to the variable num.

# fh = open("travel_plans.txt", "r")
# contents = fh.read()
# num = len(contents)
# print(num)

# Q2
# We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
# Find the total number of words in the file and assign this value to the variable num_words.

# fh = open("emotion_words.txt", "r")
# num_words = 0
# for line in fh:
#     num_words += len(line.rstrip().split())
#
# print(num_words)


# Q3
# Assign to the variable num_lines the number of lines in the file school_prompt.txt.
# fh = open("school_prompt.txt", "r")
# lines = fh.readlines()
# num_lines = len(lines)
# print(num_lines)

# Q4
# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
# fh = open("school_prompt.txt", "r")
# contents = fh.read()
# beginning_chars = contents[:30]
# print(beginning_chars)

# Q5
# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
# fh = open("school_prompt.txt", "r")
# lines = fh.readlines()
# print(lines)
# three = list()
# for line in lines:
#     three.append(line.split()[2])
# print(three)

# Q6
# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
# fh = open("emotion_words.txt", "r")
# lines = fh.readlines()
# print(lines)
#
# emotions = list()
# for line in lines:
#     emotions.append(line.split()[0])
# print(emotions)

# Q7
# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
# fh = open("travel_plans.txt", "r")
# first_chars = fh.read()[:33]
# print(first_chars)

# Q8
# Challenge: Using the file school_prompt.txt,
# if the character ‘p’ is in a word, then add the word to a list called p_words.
fh = open("school_prompt.txt", "r")
lines = fh.readlines()
print(lines)

p_words = list()
for line in lines:
    for word in line.split():
        if 'p' in word:
            p_words.append(word)

print(p_words)