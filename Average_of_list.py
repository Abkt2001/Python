def average(list1):
    sum = 0
    for x in list1:
        sum = sum+x
    avg = sum/len(list1)
    return avg

list2 = [10,20,30,40,50]
print(average(list2))