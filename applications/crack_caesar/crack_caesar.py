# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import os
fileTxt = ''
path = os.getcwd() + '/applications/crack_caesar/ciphertext.txt'
with open(path) as f:
    fileTxt = f.read()

commonFreq = [
    'E', 
    'T', 
    'A', 
    'O', 
    'H', 
    'N', 
    'R', 
    'I', 
    'S', 
    'D', 
    'L', 
    'W', 
    'U', 
    'G', 
    'F', 
    'B', 
    'M', 
    'Y', 
    'C', 
    'P', 
    'K', 
    'V', 
    'Q', 
    'J', 
    'X', 
    'Z'
]

cipherFreq = {}

for i in commonFreq:
    cipherFreq[i] = 0

for i in fileTxt:
    if i in cipherFreq:
        cipherFreq[i] += 1

cipherList = []
for i in commonFreq:
    cipherList.append( (i, cipherFreq[i]) )

cipherList.sort(
    key = lambda c: (-c[1], c[0])
)

key = {}

for i in range(0, len(cipherList)):
    key[cipherList[i][0]] = commonFreq[i]

newtxt = ''
for i in fileTxt:
    if i in key:
        newtxt += key[i]
    else:
        newtxt += i

print(newtxt)

# order letters from ciphertext.txt case non-sensitive by frequency
# number of times letter occurs / total letters

# loop through both freqs, aligning key: value as cipherFreq: freq
# loop through ciphertext creating a new string with each cipherFreq letter replaced by freq