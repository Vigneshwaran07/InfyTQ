from collections import Counter
a = input()
re = ''
lwr = sorted(list(Counter(a.lower()).keys()))
acount = Counter(a)
for i in lwr:
    re += i.upper()*acount[i.upper()]
    re += i*acount[i]
print(re)
