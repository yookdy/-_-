#baekjoon string 11720 8/13
#처음에 값을 string으로 받고 리스트로 만든뒤 for문을 이용해서  int로 변환 후 값을 r에 더한 값을 저장하는 방식으로 구현
n=(input())
pri=list(n)
r=0
for i in range(len(n)):
    r+=int(pri[i])
print(r)
