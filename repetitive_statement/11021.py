#baekjoon repetitive statement 11021.py
#map을 이용해서 두 수를 받고 그 길이 만큼 반복문을 돌리고 문자열 포멧팅을 이용해서 인덱스 번호와 합을 출력하는 방식으로 구현
T=int(input())
list1=[]
for _ in range(T):
    a, b= map(int, input().split())
    list1.append(a+b)
for i in range(len(list1)):
    print(f"Case #{i+1}: {list1[i]}")
