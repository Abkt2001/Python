def sortn(l1):
    for i in range (0,len(l1)):
        for j in range (0,len(l1)-1):
            if l1[j]<l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]
    return l1
    
    
    
    
l = [1,2,3,4,5,6,7,8,9,9,9]

l2 = sortn(l)
fl = l2[0]
print('Sorted list is ',l2)
for i in range (1,len(l2)):
    if l2[i]<fl:
        print('Second largest number is {}'.format(l2[i]))
        break
    else:
        continue
        
    