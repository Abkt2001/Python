def smaller(list2,num):
    list3 = []
    for x in list2:
        if x<num:
            list3.append(x)
    return list3 

list1 = [1,2,3,4,5,6,7,8,9,0]
element = 5
small = smaller(list1,5)
print(small)
            