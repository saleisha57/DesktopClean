#Kruskal

array = {
		'vertices': ['a','b','c'],
		'edges': set([(2,'a','b'),
		              (1,'a','c'),
					  (3,'b','c')])
		}
		
def kruskal():
	answer = []
	for v in graph[vertices]:
		make_set()
	for (w,v) in array[edges]:
		if find_set(w) != find_set(v):
			# answer = answer UNION {(w,v)}
			UNION(w,v)
	return answer

output = kruskal()

print(output)