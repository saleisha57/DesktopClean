f = open('greedy_c.txt')
file_stuff = f.read()
args = [p.strip() for p in file_stuff.splitlines()]
f.close()

number = int(args[0])
number_1 = int(args[1])
dna_s = args[2:]
counts = {'A':0, 'C':1, 'G':2, 'T':3}


def h_distance(pat, st):
    n = 0
    if len(pat) == len(st):
        for x, i in zip(st, pat):
            if x != i:
                n += 1
    return n


def set_profile(motifs):
    columns = [''.join(something) for something in zip(*motifs)]
    return [[float(col.count(n)+4) / len(col) for n in 'ACGT'] for col in columns]



def get_score(motifs):
    score = 0
    for x in range(len(motifs[0])):
        mot = ''.join([motifs[i][x] for i in range(len(motifs))])
        score += min([h_distance(mot, h*len(mot)) for h in 'ACGT'])
    return score



def calc(kmer, profile):
    score = 1.0
    for i, c in enumerate(kmer):
        score *= profile[i][counts[c]]
    return score



def probable(motif, k, profile):
    best = ''
    stuff = []
    best_prob = -1
    for i in range(len(motif)-k+1):
        kmer = motif[i:i+number]
        s = calc(kmer, profile)
        if s > best_prob:
            stuff.append(kmer)
            best_prob = s
            best = kmer
    return best



def do_work(dna, k, t):
    best_motifs = []
    test = []
    for d in dna:
        best_motifs.append(d[0:0+k])
    best_score = get_score(best_motifs)
    l = len(dna[0])
    for x in range(l-k+1):
        mo = []
        mo.append(dna[0][x:x+k])
        for i in range(1, t):
            profile = set_profile(mo)
            mo.append(probable(dna[i], k, profile))
        if get_score(mo) < best_score:
            best_score = get_score(mo)
            best_motifs = mo
    return str(' '.join(best_motifs))



a = do_work(dna_s, number, number_1)
print(a)
