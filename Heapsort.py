#Heapsort (Referencing the book for makeHeap, and https://www.geeksforgeeks.org/heap-sort/ for heapsort)

array = [1,2,3,4,5,6]

def makeHeap(arr):
	n = len(arr)
	for x in range(n//2,1,-1):
		k = x
		v = arr[k]
		heap = False
		while (not heap) and ((2*k) <= n):
			j = (2*k)
			if j < n:
				if arr[j] < arr[j+1]:
					j += 1
				if v >= arr[j]:
					heap = True
				else:
					arr[k] = arr[j]
					k = j
		arr[k] = v
	return arr
	
def heapsort(a):
	holder = 0
	for x in range(len(a)//2,1,-1):
		makeHeap(a)	
	for i in range(len(a)-1,1,-1):
		holder = a[0]
		a[0] = a[i]
		a[i] = holder
		makeHeap(a)
	return a

answer = heapsort(array)
print(a)

