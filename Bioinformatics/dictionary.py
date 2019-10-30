f = open('test.txt')
file_stuff = f.read()
args = [p.strip() for p in file_stuff.splitlines()]
f.close()

print(args[0])
