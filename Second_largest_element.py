def max_element(l1):
    for x in range(0,len(l1)):
        for x in range(0,len(l1)-1):
            if l1[x]<l1[x+1]:
                l1[x],l1[x+1]=l1[x+1],l1[x]
    return l1[0]

def sec(l1):
    larg = max_element(l1)
    if len(l1)<=1:
        return None
    slar=None
    for x in l1:
        if x != larg:
            if slar == None:
                slar = x
            else:
                slar=max(slar,x)

l = [12,76,90,63,26,76,7,15,99,99]
print(sec(l))