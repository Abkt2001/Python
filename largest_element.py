def larg(l1):
    for x in range(0,len(l1)):
        for x in range(0,len(l1)-1):
            if l1[x]<l1[x+1]:
                l1[x],l1[x+1]= l1[x+1],l1[x]   
    return l1[0]

def large(l1):
    a = l1[0]
    for i in range(1,len(l1)):
        if l1[i]>a:
            a = l1[i]
    return a

l = [11,72,38,45,65,64,72,86,29]
print(larg(l))
print(large(l))