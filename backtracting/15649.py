#baekjoon Backtracking 15649 11/18
#두 변수를 받고 순열 리스트를 생성을 하고 백트래킹으로 출력하는 길이에 맞으며뉴 출력을 하고 중복을 제거하는 방식으로 구현을 함

def dfs():
    #출력을 하는 부분
    if len(s) == m: #저장한 리스트가 m과 같은 길이를 가지면 리턴을 함
        print(' '.join(map(str, s)))
        return
    
    #중복을 확인하는 부분--백트래킹 기술이 들어가는 부분
    for i in range(1, n+1):
        if visited[i]: #들어간 숫자를 체크하는 if문
            continue

        visited[i] = True #안 담겨있으면 s에 넣는 역활을 함
        s.append(i)

        dfs() #백트래킹

        s.pop() #리스트의 길이를 줄여주는 역활을 함
        #미리 저장된 변수를 제거하는 역활을 함
        visited[i] = False
        #리스트에서 제거된 숫자를 다시 사용 할 수 있게 변경을 해주는 역활을 함
        #다음 숫자로 넘어가게 만들어주는 역활을 함
            

n, m = map(int, input().split())
s = [] #순열을 저장을 하는 리스트
#들어간 숫자를 체크하는 의미 -> 순열 생성
visited = [False] * (n+1)
dfs()