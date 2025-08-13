#baekjoon string 9086 8/13
#각 string값을 받고 리스트에 저장한 후에 문자열 슬라이싱을 사용해서 문자의 처음과 마지막 값을 추출해서 더한 후 출력하는 방식으로 구현
a=int(input())
pri=[]
for _ in range(a):
   b=input()
   pri.append(b)
for i in range(a):
    if(len(pri[i])<2):
        pri[i]=pri[i]+pri[i]
        print(pri[i])
    else:
        pri[i]=pri[i][0]+pri[i][len(pri[i])-1]
        print(pri[i])
   