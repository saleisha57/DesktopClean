f = open('test_file.txt', 'r')
o = open('out.txt', 'w')
number = 0
for line in f:
    number += 1
    if number%2 == 0:
        o.write(line)

o = open('out.txt', 'r')
for x in o:
    print(x)
