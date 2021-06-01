def reverse(l1):
    for x in range (len(l1)-1,-1,-1):
        a = l1[x]
        l1.append(a)
        l1.pop(x)
    return l1

def rever(l1):
    l1.reverse()
    return l1

def revers(l1):
    l2=list(reversed(l1))
    return l2


l = [1,2,3,4,5,6,7]

print(revers(l))