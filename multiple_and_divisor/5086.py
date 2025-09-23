#baekjoon mutiple and divisor 5086 9/23
#약수와 배수인지의 경우를 나눈다음0,0이 입력이 들어오면 종료가 되기에 for문이 아닌 while문을 사용해서 루프를 돌리는 방식으로 구현

while True:
    a, b =map(int, input().split())
    if a==0 and b==0:
        break
    elif a%b==0:
        print("multiple")
    elif b%a==0:
        print("factor")
    else:
        print("neither")


