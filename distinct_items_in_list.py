def distinct(s1):
    s2 = []
    for x in s1:
        if x not in s2:
            s2.append(x)
    return len(s2)

def distinct1(s1):
    res = 1
    count = 1
    
    if len(s1)==0:
        return 0
    else:
        for x in range(res,len(s1)):
            # r = list(s1[:res])
            if s1[x] not in s1[:res]:
                count = count + 1
            res += 1
        return count
             
def distinct2(s1):
    return len(set(s1))

s =[1,2,3,3]

print(distinct(s))
print(distinct1(s))
print(distinct2(s))