from  collections import deque
def rotate_n3(l1,n):
    dq = deque(l1)
    dq.rotate(-n)
    l1 = dq
    return l1


def rotate_n4(l1,n):
    l1 = l1[n:] + l1[0:n]
    return l1



def rotate_n(l1,n):
    for i in range(1,n+1):
        tmp=l1[0]
        for x in range (0,len(l1)-1):
            l[x] = l[x+1]
        l1[len(l1)-1] = tmp
    return l1

def rotate_n1(l1,n):
    for x in range (1,n+1):
        l1.append(l1.pop(0))
    return l1

def rotate_n2(l1,n):
    for x in range (1,n+1):
        l1 = l1[1:] + l1[0:1]
    return l1

l = [1,2,3,4,5,6,7,8,9]
times = 9
print('Left rotate by {} times is '.format(times),rotate_n4(l,times))