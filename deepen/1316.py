#baekjoon deepen 1316 8/31
#단어를 입력받은 후 리스트로 전환한뒤 각 인덱스의 값에서 연속적으로 되는 상황은 continue로 넘기고 그 외의 값이 나오면 
# break로 멈추고 조건문을 통해서 else문에 도달하면 re의 값을 1늘리는 방식으로 구현함
a=int(input())
re=0
for _ in range(a):
    b=input()
    li=list(b)
    for i in range(len(li)-1):
            if li[i]==li[i+1]:
               continue
            elif li[i] in li[i+1:]:
                break
    else:
        re+=1
print(re)