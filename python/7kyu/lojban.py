loj = dict()
loj['pa'] = 1
loj['re'] = 2
loj['ci'] = 3
loj['vo'] = 4
loj['mu'] = 5
loj['xa'] = 6
loj['ze'] = 7
loj['bi'] = 8 
loj['so'] = 9
loj['no'] = 0
        
def convert_lojban(lojban):
    num = loj.keys()
    ban = list(lojban) 
    word = ''
    res = ''
    while ban:
        word += ban[0]
        if word in num:
            res += str(loj[word])
            word = ''
        del ban[0]
    return int(res)
