#baekjoon repetitive statement 2439 8/11
#파이썬의 format을 이용하지 않고 문자열을 리스트로 이용해서 나타내는 방식으로 구현
a=int(input())
list1=[" "]*a
for i in range(a):
    list1[a-i-1]="*"
    print("".join(list1))