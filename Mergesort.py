# Referenced the pseudocode from:  https://en.wikipedia.org/wiki/Merge_sort
import random

array = []

for n in range(0,100):
	array.append(random.randint(1,1000))

middle = 0
left = []
right = []

# Merge the arrays back together.
def mergeback(l,r):
	results = []
	while len(l) > 0 and len(r) > 0:
		if l[0] <= r[0]:
			results.append(l[0])
			l.pop(0)
		else:
			results.append(r[0])
			r.pop(0)
	while len(l) > 0:
		results.append(l[0])
		l.pop(0)
	while len(r) > 0:
		results.append(r[0])
		r.pop(0)
	return results

# Divide the array in half and recursively sort.
def mergesort(a):
	if len(a) <= 1:
		return a
	middle = int(len(a)/2)
	left = a[:middle]
	right = a[middle:]
	left = mergesort(left)
	right = mergesort(right)
	return mergeback(left,right)

answer = mergesort(array)
print(array, "\n")
print(answer)
