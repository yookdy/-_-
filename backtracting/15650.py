#baekjoon backtracking 15650 11/24
#백트래킹 기술을 쓰는데 i를 기준을 이용을 해서 i+1로 다시 함수를 작동을 시키면서 리스트에 값을 추가하면서 작동하는 방식으로 구현

n, m = map(int, input().split())
s = []

def dfs(re):
    if len(s) == m: 
        print(' '.join(map(str, s)))
        return
    for i in range(re,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)