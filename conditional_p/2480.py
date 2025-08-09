#baekjoon conditional probability 2480 8/9
#세 개의 수를 받고 조건문을 이용해서 같은 수에 따른 출력값을 구하는 방식으로 구현
a,b,c=map(int, input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b or b==c or a==c:
    if a==b:
        print(1000+a*100)
    elif b==c:
        print(1000+b*100)
    else:
        print(1000+c*100)
else:
    print(max(a,b,c)*100)
