# Your code here
def isLetter(l):
    if ord(l) > 64 and ord(l) < 123:
        return True
    else:
        return False

fileTxt = ''

import os

with open(os.getcwd() + '/applications/histo/robin.txt') as f:
    fileTxt = f.read()

cache = {}
word = ''

for i in fileTxt:
    if isLetter(i):
        word += i.lower()
    else:
        if len(word):
            if word in cache:
                cache[word] += 1
            else: 
                cache[word] = 1
            word = ''

words = []

for k, v in cache.items():
    words.append((v, k))

words.sort(
    key = lambda w: (-w[0], w[1])
)

wordLength = len('a                ')

for i in words:
    spaces = ' ' * (wordLength - len(i[1]))
    hashes = '#' * i[0]

    print(i[1] + spaces + hashes)


# 1] count words into a hash table
# 2] splay values into list
# 3] sort list by 1] count 2] alphabet
# 4] format
# 4a] word + spaces add up to same number each time
# 4b] place the number of hashTags corresponding to the number of word occurrences