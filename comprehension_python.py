l1 = [1,2,3,4,5,6,7,8,9,0]

odd = [x for x in l1 if x%2!=0]
even = [x for x in l1 if x%2 ==0]
print(odd)
print(even)

element = 5
smaller = [x for x in l1 if x<element]
print(smaller)

