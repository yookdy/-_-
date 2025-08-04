#baekjoon one dimensional ordering 10810
#두 수를 받고 for문을 이용해서 i,j,k를 입력받고 리스트에 k를 반복해서 다시 올리는 방식으로 구현
a, b = map(int, input().split())
list1=[0]*a
for d in range(b):
    i, j, k= map(int, input().split())
    for c in range(i-1,j):
        list1[c]=k
print(*list1)