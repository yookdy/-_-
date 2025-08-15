#baekjoon string 10809 8/15
#알파벳 순서를 리스트로 바꾸고 w에 있는 알파벳이 알파벳 리스트에 있는지 확인한 후 있을 때 i값을 고정시킨뒤
#j에대한 for문을 이용해서 w에 있는 알파벳을 번호를 찾고 없을 때는 -1로 변환하는 방식으로 구현
w=input()
al="abcdefghijklmnopqrstuvwxyz"
l1=list(al)
for i in range(len(l1)):
    if l1[i] in w:
        for j in range(len(w)):
            if w[j]!=l1[i]:
                j+=j
            else:
                l1[i]=j   
    else:
        l1[i]=-1
print(*l1)