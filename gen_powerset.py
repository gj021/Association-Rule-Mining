import pickle
import numpy as np
from powerset import *
from generate import k_itemset 

pkl_file=open("items.pkl","rb")

items=pickle.load(pkl_file)

hash_table=dict()

count=1
for i in items_list:
	hash_table[count]=i
	count=count+1

max_length=len(items_list)

def csupport(lists):
	try:
   		intersected = set(lists[0]).intersection(*lists)
	except ValueError:
		intersected = set()
	return len(intersected)

superdict = dict()

for i in hash_table:
	l = [i]
	superdict[tuple(l)]=[csupport([items[hash_table[i]]]),1]

true_candidates = []
candidates=	[]

for i in hash_table:
	l=[i]
	candidates.append(l)

for i in range(1,max_length):
	print(candidates)
	true_candidates=[]
	candidates=k_itemset(candidates,i)
	# print(candidates)
	for j in candidates:
		flag = 1
		print(j)
		# s=superdict[tuple(j)]	
		# if s[1]!=-1:
		l = powerset(j, len(j)-1)
		for p in l:
			if  tuple(p) in superdict:
				continue
			else:
				print("here")
				flag=0
				break
		if flag==1:
			sup=[]
			for k in j:
				sup.append(items[hash_table[k]])
			if csupport(sup)>=20:
				superdict[tuple(j)]=[csupport(sup),len(j)]
				true_candidates.append(j)
						
	candidates=true_candidates		
print(superdict)


  