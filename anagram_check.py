def anag(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        s11 = sorted(s1)
        s22 = sorted(s2)

        if s11==s22:
            return True
    return False

def anag1(s1,s2):
    if len(s1)!= len(s2):
        return False
    
    count = [0]*256
    for i in range (0,len(s1)):
        count[ord(s1[i])]  += 1
        count[ord(s2[i])]  -= 1
    for i in count:
        if i!=0:
            return False
    return True

s1 = "silent"
s2 = "listen"
print(anag1(s1,s2))