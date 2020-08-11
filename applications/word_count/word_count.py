#move through the string
#notice when a word starts


def word_count(s):

    ignore = set()

    ignore.add('"')
    ignore.add(':')
    ignore.add(';')
    ignore.add(',')
    ignore.add('.')
    ignore.add('-')
    ignore.add('+')
    ignore.add('=')
    ignore.add('/')
    ignore.add("\r")
    ignore.add("\n")
    ignore.add("\t")
    ignore.add("\\")
    ignore.add('|')
    ignore.add('[')
    ignore.add(']')
    ignore.add('{')
    ignore.add('}')
    ignore.add('(')
    ignore.add(')')
    ignore.add('*')
    ignore.add('^')
    ignore.add('&')

    ignore.add(' ')

    words = {}

    word = ''
    
    for i in s:

        if i in ignore:
            if len(word): 
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
                word = ''

        if i not in ignore:
            
            word += i.lower()

    if len(word): 
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))