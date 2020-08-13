def no_dups(s):

    encountered = set()
    word = ''

    i = 0
    wordArr = s.split(' ')

    keepers = []

    for i in wordArr:
        if i in encountered:
            continue
        else:
            encountered.add(i)
            keepers.append(i)

    return ' '.join(keepers)
    # while i < len(s):
    
    #     if isLetter(s[i]):
    #         word += s[i]
    #         i += 1
    #     else: # first encounter of non-letter
    #         if len(word):
    #             if word in encountered: 
    #                 i = i - len(word)
    #                 word = ''
    #             encountered.add(word)
    #             word = ''
    #         else:
    #             i += 1

        
    
    print('enc', encountered)

# determine where the word starts/ends by spacing
# hold the previously identified word in memory
# replace whenever the next word is found if the word is different
# if it is the same, remove the word + space after the word[space before is untouched]
def isLetter(l):
    if ord(l) > 64 and ord(l) < 123:
        return True
    else:
        return False
    
if __name__ == "__main__":
    # print('a', ord('a'))
    # print('A', ord('A'))
    # print('z', ord('z'))
    # print('Z', ord('Z'))
    # print(no_dups(""))
    # print(no_dups("hello"))
    # print(no_dups("hello hello"))
    # print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))

# between 65 inclusive and 122 inclusive