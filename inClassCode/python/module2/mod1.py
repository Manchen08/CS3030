#!/usr/bin/env python3
# Task: Count how many words are in a file
# Getting file from the web with urlopen
from urllib.request import urlopen

listWords = []
with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/snippet.txt") as story:
    for line in story:
        line_words = line.split()
        for word in line_words:
           listWords.append(word.decode("utf-8"))

print(listWords)
print("Total count is ", len(listWords))
exit(0)
