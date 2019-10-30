s = 'GCGCG'
other = 'GCG'
number = 0

def pattern(t, p):
    for x in range(x, (p.len()-t.len())):
        if p in t:
            number += 1
print(number)
