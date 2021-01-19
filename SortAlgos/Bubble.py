# Bubble sort 
# Time complexity O(n^2)

print('Enter the array')
a = [int(i) for i in input().split()]
for i in range(0, len(a)):
    for j in range(0, len(a)-i-1):
        if a[j + 1] > a[j]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
a = a[::-1]
