from string import ascii_lowercase as lower
from string import ascii_uppercase as upper

def gimme_the_letters(sp):
    _start, _end = sp.split('-')
    if _start.islower():
        first = lower.index(_start)
        last = lower.index(_end)
        return lower[first: last+1]
    else:
        first = upper.index(_start)
        last = upper.index(_end)
        return upper[first: last+1]
