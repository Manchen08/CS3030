#!/usr/bin/env python3
# Task: Count how many words are in a file
# Getting file from the web with urlopen
import sys

from urllib.request import urlopen

def fetch_words(url):
    """
    Fetch a list of words from a url
    Args: 
        url -> The URL of a UTF-8 text document.
    Return:
        A list of strings containing the words from the document.
    """
    listWords = []
    with urlopen(url) as story:
        for line in story:
            line_words = line.split()
            for word in line_words:
               listWords.append(word.decode("utf-8"))
    return listWords

#print(listWords)
#print("Total count is ", len(listWords))

def print_items(items):
    """
    Print items one per line
    Args:
        An iterable series of printable items
    Returns:
        nothing
    """
    for item in items:
        print(item)

# if it's being ran on its own, run
def main():
    """
    Print each word from a text document from a given URL.
    Usage:
        python3 words.py <URL>
    """
    # url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/snippet.txt"
    url = sys.argv(1)
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main()
    exit(0)


