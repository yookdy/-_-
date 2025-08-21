n=int(input())
m=2*n-1
li=[0]*m
for i in range(n):
    li[i]="*"*(2*i+1)
for j in range(n,m):
    li[j]=li[m-j-1]
for k in range(m):
    print(f"{li[k]:^{m}}")

