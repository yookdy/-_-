#baekjoon repetitive statement 25313
#a의 4 나눈값만큼 long을 리스트의 0번째 인덱스에 넣는 형식
a=int(input())
list1=["int"]
b=a/4
for _ in range(int(b)):
    list1.insert(0, "long")
print(*list1)