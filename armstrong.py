a=int(input("enter the number"))
s=0
z=1
d=0
while d==a:
    d=a%(10**z)
    print(d)
    z+=1
    s+=1
