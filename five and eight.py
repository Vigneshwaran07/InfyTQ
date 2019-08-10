a = input().replace(',','')
t = 0
s,e = 0,0
f1,f2 = 0,0
for ind,i in enumerate(a):
    if(i=='5' and f1==0 and f2==0):
        f1 = 1
        f2 = 1
        s = ind
    elif(i=='8' and f1==1):
        t += int(a[s:ind+1])
        f1 = 0
        f2 = 0
    elif(f1==0 and f2==0):
        t += int(i)
if(f1==1 and f2==1):
    t += sum(map(int,list(a[s:])))
print(t)
