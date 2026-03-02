#baekjoon DeepenTwo 25192 2026/3/2
#set를 이용해서 중복되는 값을 제거하고 ENTER이 입력될때마다 set을 초기화하는 방식으로 구현

N = int(input())
S = 0
NS = set()
for i in range(1, N+1):
    s = input()
    if s == "ENTER":
        NS.clear()
    elif s not in NS:
            NS.add(s)
            S += 1
print(S)