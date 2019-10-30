st = 'ACGATGTAGACCCGACGTTTGACGATGTAGACCCGGTCTGAAACACGATGTGTCTGAAACACGATGTACGTTTGGTCTGAAACGTGGCCAAACGATGTACGTTTGAGACCCGAGACCCGAGACCCGACGTTTGACGATGTAGACCCGAGACCCGACGATGTGTCTGAAACGTGGCCAAACGATGTACGATGTACGTTTGACGATGTACGTTTGGTCTGAAACAGACCCGAGACCCGACGTTTGGTCTGAAACGTGGCCAAAGACCCGACGTTTGACGATGTGTCTGAAACACGTTTGGTCTGAAACACGATGTACGTTTGGTGGCCAAGTCTGAAACACGTTTGACGTTTGAGACCCGACGATGTGTGGCCAAACGATGTGTCTGAAACAGACCCGAGACCCGGTCTGAAACGTCTGAAACACGTTTGAGACCCGGTGGCCAAACGATGTGTCTGAAACAGACCCGACGTTTGAGACCCGGTGGCCAAGTCTGAAACGTCTGAAACGTGGCCAAGTGGCCAAACGATGTAGACCCGGTGGCCAAGTGGCCAAGTCTGAAACACGATGTACGATGTACGTTTGACGTTTGAGACCCGACGATGTGTGGCCAAAGACCCGACGATGTAGACCCGGTGGCCAAACGATGTGTCTGAAACACGTTTGGTGGCCAAACGATGTAGACCCGAGACCCGACGATGTGTGGCCAAGTCTGAAACGTCTGAAACACGTTTGACGTTTGAGACCCGAGACCCGACGTTTGGTCTGAAACGTGGCCAAAGACCCGGTCTGAAACAGACCCGGTGGCCAAGTGGCCAAACGTTTG'
k_len = 13

num_k = len(st) - k_len + 1
number = 0
my_dictionary = {}

def do_work(s,n):
    for x in range (num_k):
        w = s[x:x+n]
        my_dictionary[w] = my_dictionary.get(w, 0)+1
    number = max(my_dictionary.values())

    answer = [i[0] for i in my_dictionary.items() if i[1] == number]
    return ' '.join(answer)

a = do_work(st, k_len)
print(a)
print('I love Aleisha')

quote = ("Everyone is unique")

multi_line_quote = ''' in 
there own way
'''

print((quote) + (multi_line_quote)+ "\n\n\n")

#/n/(3)

print("OMG IT FACKIN WORKED")

grocery_list = ['tomatoes','pasta','meat', 'soda', 'cheese']

allergy_list = ['pasta','cheese'] 

for item in grocery_list:
	for AL in allergy_list:
		if AL == item:
			print(item)
		
print('\n\n\n\n\n\n')

print(grocery_list[0] + "\n\n\n")

for x in range(0, len(grocery_list)):
	if x != 2 and x != 4:
		print(grocery_list[x])

#for item in grocery_list:
#	if item == 'soda':
grocery_list.pop(3)
print(grocery_list)
grocery_list.insert(0,'soda')
print(str(grocery_list) + '\n')

val = True

thisdict = {'Animal':"Cat","Age":3, 'HasOwner':True}
thatdict = {'Animal':"Dog","Age":7, 'HasOwner':False}

print(thisdict,'\n', thatdict)

print(thisdict["Animal"],thisdict["HasOwner"])
print(thatdict["Animal"],thatdict["HasOwner"])