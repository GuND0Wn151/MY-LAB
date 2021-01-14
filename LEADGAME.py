l=[]
a0=0
n0=0
for _ in range(int(input())):
      ll=[int(i) for i in input().split()]
      l.append([ll[0]+a0,ll[1]+n0])
      a0+=ll[0]
      n0+=ll[1]
#print(l)
t=[abs(i[0]-i[1]) for i in l]
t1=[i[0]-i[1] for i in l]
#print(t,t1)
ans=max(t)
ind=t.index(ans)
if t1[ind]>0:
      print(1,ans)
else:
      print(2,ans)

