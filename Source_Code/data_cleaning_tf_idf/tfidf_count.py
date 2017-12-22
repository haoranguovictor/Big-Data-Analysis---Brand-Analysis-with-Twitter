# *************************************************
#                                                 *
#                TF-IDF Count                     *
#                Team: BDII                       *
#                Course:EECS6893                  *
#               Columbia University               *
#                                                 *
# *************************************************

# *************************************************
# **********TF-IDF Funcitons Defination************
# *************************************************
import math
import pandas as pd
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

path1 = "" #add your own file
path2 = ""
path3 = ""
path4 = ""

# *************************************************
# ****************Reading Files********************
# *************************************************
#..... more files

df = [None]*4
df[0]=pd.read_csv(path1, header=None, error_bad_lines=False, sep=",")
df[1]=pd.read_csv(path2, header=None, error_bad_lines=False, sep=",")
df[2]=pd.read_csv(path3, header=None, error_bad_lines=False, sep=",")
df[3]=pd.read_csv(path4, header=None, error_bad_lines=False, sep=",")
bloblist = []

#print(df[0][2])

# *************************************************
# ****************Tweet Cleaning*******************
# *************************************************

from tweet_cleaning import *
for i in range(4):
    temp = ''
    for row in df[i][2]:
        #print(row)
        obj=tweet_cleaning()
        x = obj.cleaning(str(row))
        temp+=x
    print(temp)
    bloblist.append(tb(temp))

# *************************************************
# *********TF-IDF counting with TextBlob***********
# *************************************************
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:5]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
