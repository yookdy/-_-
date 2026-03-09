# baekjoon DeepenTwo 2108 26/03/09
# 각각의 평균, 중앙값, 최빈값, 범위를 구하는 문제로 파이썬 메서드를 사용하여 각각의 경우를 나눠서 수를 구하는 방식으로 구현
import sys

input = sys.stdin.readline
N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()

S = sum(arr) / N
print(round(S))

M = arr[len(arr)//2] if len(arr) % 2 == 1 else (arr[len(arr)//2 - 1] + arr[len(arr)//2]) / 2
print(M)


MND = dict()
for j in arr:
    if j in MND:
        MND[j] += 1
    else:
        MND[j] = 1

mx = max(MND.values())
mx_dic = []

for i in MND:
    if mx == MND[i]:
        mx_dic.append(i)

mx_dic.sort()

if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])

# 범위
MA = arr[len(arr)-1] - arr[0]
print(MA)