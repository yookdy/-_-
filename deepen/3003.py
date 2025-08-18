#baekjoon deepen 3003 8/18
#6개의 값을 받은 뒤 리스트로 변환한고 기본 체스 말 갯수의 리스트의 각각의 인덱스에 해당하는 값끼리 뺀 값을 리스트로 저장하고 출력하는 방식으로 구현
lst = list(map(int, input().split()))
pri=[1,1,2,2,2,8]
for i in range(6):
    pri[i]=pri[i]-lst[i]
print(*pri)