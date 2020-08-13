# Your code here
import math

cache = {}
facCache = {}

def slowfun(x, y):
    if (x, y) in cache: return cache[(x, y)]

    v = math.pow(x, y)
    if v in facCache: v = facCache[v]
    else: 
        facCache[v] = math.factorial(v)
    v = facCache[v]
    v //= (x + y)
    v %= 982451653

    cache[(x, y)] = v
    return v

# def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here



# Do not modify below this line!
import random
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
