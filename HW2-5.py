#Using this site as reference for python stacks:  https://stackoverflow.com/questions/35206372/understanding-stacks-and-queues-in-python
from collections import deque

#Setting up all the variables.
n = input("Enter a number for the number of disks: ")
fi = deque()
au = deque()
la = deque()			

#Running the operations on the stacks.
def towers():
	for x in range(0,int(n)):
		fi.append(x+1)
		au.append(0)
		la.append(0)
	for r in range(0, int(n)):
		if fi[r] > au[r]:
			au.pop()
			au.appendleft(fi.popleft())
			fi.append(0)
		if fi[r] > la[r]:
			la.pop()
			la.appendleft(fi.popleft())
			fi.append(0)
		if au[r] > la[r]:
			la.pop()
			la.appendleft(au.popleft())
			au.append(0)
		if la[r] < fi[r]:
			fi.pop()
			fi.pop()
			fi.appendleft(la.popleft())
			la.append(0)
			fi.append(0)
		if la[r] < au[r]:
			la.pop()
			la.appendleft(au.popleft())
			au.append(0)

towers()

#Print out the stacks.
print(fi)
print(au)
print(la, "\n")