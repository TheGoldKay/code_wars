def reduce(txt, kind):
    count = 0
    for item in txt:
        if kind != item:
            return count
        count += 1
    return count
        
def same_length(txt):
    if len(txt) == 0:
        return True
    if txt[0] == '0':
        return False 
    ones = reduce(txt, '1')
    print(ones)
    txt = txt[ones:]
    zeros = reduce(txt, '0')
    print(zeros)
    if ones == zeros:
        return same_length(txt[zeros:])
    else:
        return False
    
