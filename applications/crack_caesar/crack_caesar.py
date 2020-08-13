# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

cipherFreq = []

# order letters from ciphertext.txt case non-sensitive by frequency
# number of times letter occurs / total letters

# loop through both freqs, aligning key: value as cipherFreq: freq
# loop through ciphertext creating a new string with each cipherFreq letter replaced by freq