#baekjoon one dimensional arrangement 5597 8/8
#for문을 이용해서 28명의 번호를 입력받고 두번째 for문과 파이썬 내장함수를 이용해서 리스트 안에 없는 번호를 찾아서 새 리스트에 넣고 최소값과 최대값을 출력하는 방식으로 구현
#파이썬은 내장함수로 쉽게 풀리기에 다른 언어로 구현해보기
list1=[]
prilist=[]
for _ in range(28):
    a=int(input())
    list1.append(a)
for i in range(30):
    if i+1 not in list1:
        a=i+1
        prilist.append(a)
print(min(prilist))
print(max(prilist))
