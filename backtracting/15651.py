#baekjoon backtracking 15651 11/26
#15650에서 1를 함수를 보낸것과 달리 처음부터 1부터 반복문을 시작을 해서 중복이 되게 리스트에 추가되게 하는 방식으로 구현

n, m = map(int, input().split())
s = []

def dfs():
    if len(s) == m: 
        print(' '.join(map(str, s)))
        return
    for i in range(1,n+1):
        s.append(i)
        dfs()
        s.pop()
dfs()