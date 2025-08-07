#baekjoon onedimensional ordering 2562 8/1
#9개의 수를 리스트로 입력받고 리스트 안에 최댓값을 구한 후 그 값의 위치를 구하는 방식으로 구현
list1 = [int(input()) for _ in range(9)]
a=max(list1)
print(a)
for i in range(len(list1)):
    if list1[i]==a:
        print(i+1)