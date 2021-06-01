def rotate(l1):
    tmp = l1[0]
    for i in range(0, len(l1)-1):
        l1[i] = l1[i+1]

    l1[len(l1)-1] = tmp
    return l1

def rotate1(l1):
    l1 = l1[1:] + l1[0:1]
    return l1

def rotate2(l1):
    l1.append(l1.pop(0))
    return l1

l = [1, 2, 3, 4, 5,6,7,8,9,10]
print('Left rotated list by one is ', rotate2(l))
