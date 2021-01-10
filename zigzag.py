a=input()
a=a[1:len(a)-1]
print(a)
b=int(input())
l=[[ 0 for _ in range(len(a)) ] for _ in range(b)]
t=b-2
#row=b
#col=len(a)
x=0
ex=0



for i in range(len(a)):
    if(ex==1):
        break
    for j in range(b):
        #print(x)
        if(x==len(a)):
            ex=1
            
            
        elif(i==0 or (i)%(b-1)==0):
            l[j][i]=a[x]
            x+=1
            
            
            
        else:
            if(t==0):
                t=b-2
            if(j==t):
                l[j][i]=a[x]
                x+=1
                t-=1
            

            
            
            
            
            
            
            
            
            
            
            
for i in range(b):
    for j  in range(len(a)):
        print(l[i][j],end="")
    print()
