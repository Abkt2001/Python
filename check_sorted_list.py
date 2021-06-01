def is_sort(l2):
    for i in range (1,len(l2)):
        if l2[i] >= l2[i-1] :
                a = 'sorted'             
        else:
                a = 'Not sorted'
                return a
    return a

def sort_2(l1):
    l2=sorted(l1)
    if l1==l2:
        return 'sorted'
    else:
        return 'Not sorted'


l1 = [12,12,12,12,15,16]
s = sort_2(l1)
if s == 'sorted':
    print('List is sorted in ascending order ',l1)
else:
    print('List is unsorted',l1)
    