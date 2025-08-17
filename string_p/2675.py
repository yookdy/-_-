#baekjoon string 2675 8/17
#받은 string값을 리스트로 만든뒤 각 인덱스 값을 n만큼 반복하게 한뒤 리스트를 값을 하나의 값으로 묶은 뒤 다른 list 안에 넣은 후 값을 출력하는 형식으로 구현
a=int(input())
pri=[]
for _ in range(a):
    n, m= map(str,input().split())
    n=int(n)
    list1=list(m)
    for i in range(len(list1)):
        list1[i]=list1[i]*n    
    pri.append(''.join(list1))
for i in range(a):
    print(pri[i])