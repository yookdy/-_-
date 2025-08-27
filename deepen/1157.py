#baekjoon deepen 1157 8/26~8/27
#문자열을 받은 뒤 알파벳을 소문자로 바꾸면서 리스크로 전환한후 딕셔너리로 알파벳과 갯수를 저장한 뒤 최대값이 여러개인지 아닌지에 따라서 ? 혹은 해당 알파벳을 대문자로 바꿔서 출력하는 방식으로 구현
#코드의 길이를 더 줄일 수 있는 방법이 있을 것 같은데 생각이 나지 않음
'''
리스트를 사용하는 방법
a=input()
al=[]
ori=list(a)
for i in range(len(ori)):
    if ori[i] not in al:
        al.append(ori[i])
alpri=[0]*len(al)
for j in range(len(al)):
    for k in range(len(ori)):
        if al[j]==ori[k]:
            alpri[j]+=1
m=0
ok=0
for l in range(len(al)):
    if alpri[l]==max(alpri):
        m=l
for k in range(len(al)):
    if alpri[k]==max(alpri):
        ok+=1
if ok>1:
    print("?")
else:
    print(al[m])
'''

#딕셔너리를 사용하는 방법
a=input()
al=list(a.lower())
di={}
for i in range(len(al)):
    if al[i] not in di:
        di[al[i]]=0
keys = list(di.keys())
for j in range(len(al)):
    for k in range(len(keys)):
        if al[j] == keys[k]:
            di[al[j]] += 1
m=0
ok=0
for l in range(len(keys)):
    if di[keys[l]] == max(di.values()):
        m=l
for k in range(len(keys)):
    if di[keys[k]] == max(di.values()):
        ok += 1
if ok > 1:
    print("?")
else:
    print(keys[m].upper())