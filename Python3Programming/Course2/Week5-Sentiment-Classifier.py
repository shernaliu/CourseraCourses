punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []

# populate positive_words list with data in txt file
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# Takes a word as input and removes punctuation in the word itself
def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return word

# strip_punctuation test cases
# print(strip_punctuation("#Amazing"))
# print(strip_punctuation("wow!"))
# print(strip_punctuation("#in.cred..ible!"))
# print(strip_punctuation("wonderful "))

# Takes a string (1 or more sentences) & calculates how many words are positive words
def get_pos(sentences):
    count = 0
    # convert to lowercase for comparison
    lower_sentences = sentences.lower()
    # remember to strip punctuations and split into a list of strings
    cleaned_sentences = strip_punctuation(lower_sentences).split(" ")
    for word in cleaned_sentences:
        if word in positive_words:
            count += 1
    return count

# get_pos test cases
# print(get_pos("what a truly wonderful day it is today! #incredible"))
# print(get_pos("what a truly Wonderful day it is today! #incredible"))
# print(get_pos("what a truly wonderful day it is today"))

# Takes a string (1 or more sentences) & calculates how many words are negative words
def get_neg(sentences):
    count = 0
    # convert to lowercase for comparison
    lower_sentences = sentences.lower()
    # remember to strip punctuations and split into a list of strings
    cleaned_sentences = strip_punctuation(lower_sentences).split(" ")
    for word in cleaned_sentences:
        if word in negative_words:
            count += 1
    return count

# get_neg test cases
# print(get_neg("what a truly wonderful day it is today! #incredible"))
# print(get_neg("The weather truely is abnormal - it's october and already snowing!"))
# print(get_neg("their departure was rather abrupt. However, it was amusing how aloof they had been."))
# print(get_neg("the weather is what it is."))

# opens the file project_twitter_data.csv containing fake generated twitter data
try:
    fh = open("project_twitter_data.csv", "r")
    lines = fh.readlines()
    fh.close()

    # create a new file and prepare to write to it
    file_out = open("resulting_data.csv", "w")

    # write header
    file_out.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")

    # ignore the first line (header)
    for line in lines[1:]:
        # split line into a list of string: tweet text, no. of retweets, no. of replies. use strip() to remove any \n
        splitted = line.split(",")
        tweet_text = splitted[0].strip()
        retweet_count = splitted[1].strip()
        replies_count = splitted[2].strip()

        # get positive and negative score on the text of the tweet
        positive_score = get_pos(tweet_text)
        negative_score = get_neg(tweet_text)

        # calculate net_score
        net_score = positive_score - negative_score

        # write to file
        file_out.write(str(retweet_count) + "," +
                       str(replies_count) + "," +
                       str(positive_score) + "," +
                       str(negative_score) + "," +
                       str(net_score) + "\n")

    file_out.close()
except Exception as ex:
    print("Unable to open file! " + str(ex))
    quit()