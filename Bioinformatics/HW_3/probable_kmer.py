f = open('pkmer.txt')
file_stuff = f.read()
args = [p.strip() for p in file_stuff.splitlines()]
f.close()

dna_s = args[0]
number = int(args[1])
profile = [map(float, l) for l in args[2:]]

stuff = []

def calc(kmer):
    print(kmer)
    for i in range(len(kmer)):
        if kmer[i] == 'A':
            stuff.append(profile[i:0])
        elif kmer[i] == 'C':
            stuff.append(profile[i:1])
        elif kmer[i] == 'G':
            stuff.append(profile[i:2])
        elif kmer[i] == 'T':
            stuff.append(profile[i:3])
    for c in stuff:
        print(c)

def do_work():
    best_p = ''
    best_prob = 0.0
    for i in range(len(dna_s)-number+1):
        if calc(dna_s[i:i+number]) >= best_prob:
            best_p = dna_s[i:i+number]
            best_prob = calc(dna_s[i:i+number])
    print(best_p)

do_work()
