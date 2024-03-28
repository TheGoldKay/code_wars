def convert_lojban(lojban):
    seq = ['no', 'pa', 're', 'ci', 'vo', 'mu', 'xa', 'ze', 'bi', 'so']
    return int(''.join([str(seq.index(lojban[i: i+2])) for i in range(0, len(lojban), 2)]))
