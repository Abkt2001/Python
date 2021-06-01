l1 = [1,2,3,5,4,7,6,9,8,0,9,2]

d1 = {x:x**3 for x in l1}
print(d1)

d2 = {x:f"ID[{x}]" for x in l1}
print(d2)

l2 = [1,2,3,4,5]
l3 = ['aman','amit','ankit','ankur','anuj']

d3 = {l2[x]:l3[x] for x in range (len(l2))}
print(f'{d3}')

d4 = dict(zip(l2,l3))
print(d4)

d5 = {y:x for x,y in d4.items()}
print(d5)
        
