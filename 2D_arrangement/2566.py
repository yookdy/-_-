#baekjoon twodimensional ordering 2566 9/3
#9x9크기의 2차원 리스트를 받고 각 인덱스값을 m과 비교해서 m에 대한 정보를 계속해서 갱신하면서 최댓값과 그 위치를 구하는 방식으로 구현
li=[]
l,r,m=0,0,0
for _ in range(9):
    pu=list(map(int, input().split()))
    li.append(pu)
for i in range(9):
    for j in range(9):
        if li[i][j]>=m:
            m=li[i][j]
            l=i+1
            r=j+1
print(m)
print(l,r)