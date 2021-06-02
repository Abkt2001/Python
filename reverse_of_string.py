def rever(st1):
    n = len(st1)
    for x in range (0,n+1):
        if x> n-x:
            return st1
        st1[x],st1[n-x-1] = st1[n-x-1],st1[x]
    return st1
def rever1(s1):
    rev = ""
    for i in s1:
        rev = i + rev
    return rev


def rever2(s1):
    return s1[::-1]


s = r"Abhishek kumar tiwari"

print(rever2(s))