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