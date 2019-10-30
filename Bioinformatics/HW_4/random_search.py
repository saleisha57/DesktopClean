import random

f = open('random.txt')
file_stuff = f.read()
args = [p.strip() for p in file_stuff.splitlines()]
f.close()

number = int(args[0])
number_1 = int(args[1])
dna_s = args[2:]
rand = random.SystemRandom()
sc = 1.0
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
    return [[float(col.count(n)+4) / float(len(col)) for n in 'ACGT'] for col in columns]

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
    r = []
    best_prob = -1
    for i in range(len(motif)-k+1):
        kmer = motif[i:i+number]
        s = calc(kmer, profile)
        if s > best_prob:
            r.append(kmer)
            best_prob = s
            best = kmer
    return best


def from_p(dna, k, pro):
    r =  [probable(d, k, pro) for d in dna]
    return r


def do_work(dna, k, t):
    best_m = []
    x = 0
    for d in dna:
        stuff = []
        for i in range(len(d)-k+1):
            word = d[i:i+k]
            stuff.append(word)
        best_m.append(rand.choice(stuff))
    best_score = get_score(best_m)
    w = best_m
    while x < 1000:
        profile = set_profile(w)
        w = from_p(dna, k, profile)
        if get_score(w) < get_score(best_m):
            best_m = w
        x += 1
    return str(' '.join(best_m))


#    #stuff = []
#    best_m = []
#    x = 0
#
#    for d in dna:
#        stuff = []
#        for i in range(len(d)-k+1):
#            word = d[i:i+k]
#            stuff.append(word)
#        best_m.append(rand.choice(stuff))
#    best_score = get_score(best_m)
#    while x < 5:
#        w = []
#        if x < 1:
#            for i in range(len(best_m)):
#                w.append(best_m[i])
#        for i in range(0, t):
#            profile = set_profile(w)
#            w.append(probable(dna[i],k,profile))
#        #print('w:', w)
#        s = get_score(w)
#        if s < best_score:
#            best_score = s
#            best_m = w
#        x += 1
#    return best_m


a = do_work(dna_s, number, number_1)
print(a)
