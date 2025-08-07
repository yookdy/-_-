#baekjoon repetitive statement 15552.py 8/5
#리스트의 길이을 받고 그 길이만큼 반복문을 돌려서 두수의 합을 리스트에 넣고 그 값을 한줄씩 출력하는 방식으로 구현
#***입력 받을떄 시간 초과 문제가 생길 수 있기에 input 대신 sys.stdin.readline()을 사용
import sys

a=int(sys.stdin.readline())
list1=[]
for _ in range(a):
    b, c = map(int, sys.stdin.readline().rstrip().split())
    list1.append(b+c)
for i in range(len(list1)):
    print(list1[i])