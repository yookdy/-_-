#baekjoon one dimensional ordering 10813 8/7
#두 수를 연속으로 받고 리스트의 길이만큼 1부터 n까지의 숫자를 순서대로 넣고 매개값을 이용해서 i-1,j-1번째 인덱스 값을 서로 바꾸는 방식으로 구현
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
