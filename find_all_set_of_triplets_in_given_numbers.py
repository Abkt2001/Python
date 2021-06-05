import itertools
def trip(s):
    list1 = list(set(itertools.combinations(s,3)))
    for x in list1:
        list2 = list(x)
        a,b,c=list2[0],list2[1],list2[2]

        if a*a + b*b == c*c or a*a == b*b + c*c or a*a + c*c == b*b:
            print(x)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20]
print("Triplets are :- ")
trip(numbers)
