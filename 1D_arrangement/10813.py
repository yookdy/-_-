n,m=map(int, input().split())
list1=[0]*n
for x in range(n):
    list1[x]=x+1
for k in range(m):
    i,j=map(int, input().split())
    c=0
    c=list1[i-1]
    list1[i-1]=list1[j-1]
    list1[j-1]=c
print(*list1)
