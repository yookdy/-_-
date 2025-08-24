#baekjoon deepen 10988 8/24
#문자열을 받은뒤 그 문자열을 뒤집은 문자열을 각각 리스트화 시킨뒤 두 for문을 이용해서 인덱스의 값이 같은지 확인하는 방식으로 구현
n=input()
li=list(n)
re=[]
l=len(li)
for i in range(l):
    re.append(li[l-i-1])
for j in range(l):
    if li[j]==re[j]:
        j=j+1
        if j==l:
            print(1)
    else:
        print(0)
        break
    