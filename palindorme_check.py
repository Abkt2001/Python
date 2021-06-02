def palin(s1):
    l = len(s1)
    low = 0
    high = l-1
    while low < high:
        if s1[low] != s1[high]:
            return False
        low = low + 1
        high = high - 1
    return True


def palin1(s1):
    if s1 == s1[::-1]:
        return True
    return False


st = "12321"
print(palin1(st))
