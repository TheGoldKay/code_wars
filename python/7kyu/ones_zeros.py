from itertools import groupby 

def same_length(txt):
    if txt[0] == '0':
        return False
    groups = [len(list(g)) for _, g in groupby(txt)]
    if len(groups)%2 != 0:
        return False
    for i in range(0, len(groups) - 1, 2):
        if groups[i] != groups[i+1]:
            return False 
    return True
