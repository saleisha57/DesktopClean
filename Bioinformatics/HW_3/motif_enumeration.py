import itertools

f = open('something.txt')
file_stuff = f.read()
args = [p.strip() for p in file_stuff.splitlines()]
f.close()

number = int(args[0])
allowed_mismatches = int(args[1])
dna_s = args[2:]

possible_kmers = [''.join(a) for a in itertools.product('ATCG', repeat=number)]

def h_distance(pat, st):
    n = 0
    if len(pat) == len(st):
        for x, i in zip(st, pat):
            if x != i:
                n += 1
    if n > allowed_mismatches:
        return False
    return True


def score(dna, mo, k):
    final_score = 0
    for r in dna:
        something = False
        for i in range(len(r)-k+1):
            if h_distance(mo, r[i:i+k]):
                something = True
                break
        if not something:
            return False
        return True


def get_m(kmer, d):
    miss = set()
    for i in itertools.combinations(range(len(kmer)), d):
        for r in possible_kmers:
            mismatches = list(kmer)
            for index, replace in zip(i, r):
                mismatches[index] = replace
            miss.add(''.join(mismatches))
    return miss


def get_kmer(dna, k, k_set):
    for d in dna:
        for x in range(len(d)-k+1):
            w = d[x:x+k]
            k_set.add(w)


def motifEnumeration(dna, k, d):
    patterns = []
    kmers = set()
    get_kmer(dna, k, kmers)
    for kmer in list(kmers):
        patterns.extend(get_m(kmer, d))

    patterns = list(set(patterns))

    top = []
    for mo in sorted(patterns):
        if score(dna, mo, k):
            top.append(mo)
    return top


a = motifEnumeration(dna_s, number, allowed_mismatches)
print(' '.join(a))
