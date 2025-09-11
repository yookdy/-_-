#baekjoon math1 2720 9/11
#각 값을 리스트로 받고 pr리스트와 ng리스트 대응하는 값끼리 나누고 계산값을 cal에 저장하고 또 그 값을 re에 저장하는 방식으로 구현
n = int(input())
ng=[]
pr=[25, 10,5,1]  
for _ in range(n):
    a=int(input())
    ng.append(a)
re=[]
for i in ng:
    cal=[]
    rem=i
    for j in pr:
        c=rem//j  
        cal.append(c)
        rem=rem%j  
    re.append(cal)
for r in re:
    print(*r)
