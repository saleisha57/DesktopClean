f = open('rec.txt')
file_stuff = f.read()
args = [p.strip() for p in file_stuff.splitlines()]
f.close()

dna_s = args[0:]

def do_work(dna):
    w = ''
    s = dna[0]
    for d in dna[1:]:
        for x in range(len(d)):
            w = d[x]
        s = s + w
    print(s)

do_work(dna_s)