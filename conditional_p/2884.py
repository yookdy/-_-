#baekjoon conditional 2884 7/29
#시간을 입력받고 45분 전으로 출력하는 방식으로 구현
h, m = map(int, input().split())
if m>=45:
    print(h, m-45)
else:
    if h==0:
        print(23, m+15)
    else:
        print(h-1, m+15)