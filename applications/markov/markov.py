import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

# 1] find all the words, place them as keys in dict
# 2] while searching out words, add any word following a word to the set stored as value to the word's key hashed index

# TODO: construct 5 random sentences
# Your code here

# randomly pick a word
# for that word, look it up and pick a word that's possible to follow
# repeat until a certain length is reached(how to determine length?)