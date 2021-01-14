def puprecu(d,n):
      if d==0:
            return 0
      elif d==1:
            return n*(n+1)//2
      else:
            return puprecu(d-1,n*(n+1)//2)
for _ in range(int(input())):
      d,n=[int(i) for i in input().split()]
      x=puprecu(d,n)
      print(x)
