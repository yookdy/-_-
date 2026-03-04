#baekjoon DeepenTwo 26069 2026/3/4
#ChongChong이 포함되면 n,m을 있는지의 여부에 따라서 set에 추가해서 set의 길이를 출력하는 방식으로 구현

N = int(input())
S=set()
for i in range(1, N+1):
    n, m = input().split()
    if n == "ChongChong" or m == "ChongChong":
        S.add(n)
        S.add(m)
    if n in S or m in S:
        S.add(n)
        S.add(m)
print(len(S))
    
    
