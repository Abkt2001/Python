# def appeear(l1):
# count = 0
# even = []
# odd = []
# for i in range (0,len(l1)):
# for j in range (1,len(l1)):
# if l1[i] == l1[j]:
# count = count+1
# if count%2 ==0 :
# even.append(l1[i])
# else:
# odd.append(l1[i])
# return even,odd
#

def appear(l1):
    odd = []
    even = []
    for x in l1:
        count = l1.count(x)
        if count % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return odd, even


l = [1, 2, 3, 3, 4, 4, 5, 6, 8, 8, 9]

odd, even = appear(l)

print('Numbers occurs even times is ', list(set(even)))
print('Numbers occurs odd time is ', list(set(odd)))
