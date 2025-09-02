#baekjoon twodimensional ordering 2738 9/2
#리스트에 map을 이용해서 열을 받고 행의 크기만큼 for문을 돌려서 2차원 리스트를 2개 만든 후 
#각 인덱스를 더한 값을 열을 기준으로 다시 리스트에 넣고 출력하는 방식으로 구현
n=[]
m=[]
pr=[]
a,b=map(int, input().split())#a=행, b=열
for r in range(a):
    pu=list(map(int, input().split()))
    n.append(pu)
for k in range(a):
    pu2=list(map(int, input().split()))
    m.append(pu2)
for i in range(a):
    ren=[]
    for j in range(b):
        ren.append(n[i][j]+m[i][j])
    pr.append(ren)
for x in pr:
    print(*x)

