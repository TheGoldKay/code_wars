from string import ascii_lowercase as lower
from string import ascii_uppercase as upper

sequence = lambda _start, _end, alpha: alpha[alpha.index(_start): alpha.index(_end)+1]

def gimme_the_letters(sp):
    _start, _end = sp.split('-')
    return sequence(_start, _end, upper) if _start.isupper() else sequence(_start, _end, lower)
