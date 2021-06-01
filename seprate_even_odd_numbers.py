def seprate(list2):
    even = []
    odd = []
    for x in list2:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    return even,odd
    # print(even)
    # print(odd)

list1 = [1,2,3,4,5,6,7,8,9,0]
# seprate(list1)
even,odd = seprate(list1)
print(odd)
print(even)
