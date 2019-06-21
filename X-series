from itertools import combinations
def cut(list1, a):
    list2 = []
    for i in list1:
        j = i[:]
        if((i[-1]+i[-2]) in a):
            j.append(i[-1]+i[-2])
            list2.append(j)
    if(len(list2)==0):
        return 1,list2
    return 0,list2
    
a = list(map(int, input().split(',')))
list1 = []
for i in combinations(a, 2):
    i = sorted(list(i))
    if((i[-1]+i[-2]) in a):
        i.append(i[-1]+i[-2])
        list1.append(i)

list2 = list1[:]
while(True):
    flag,list2 = cut(list1,a)
    if(flag==1):
        break
    list1 = list2[:]

s = []
m = 0
for i in list1:
    s += i
uniq = sorted(set(s))
for i in uniq:
    if(s.count(i)==1):
        m = i
        break
for i in list1:
    if(m in i):
        print(i)
        break
