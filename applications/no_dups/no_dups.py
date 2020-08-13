def no_dups(s):
    # Your code here

# determine where the word starts/ends by spacing
# hold the previously identified word in memory
# replace whenever the next word is found if the word is different
# if it is the same, remove the word + space after the word[space before is untouched]

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))