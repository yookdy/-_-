#
# a=input()
# al=[]
# ori=list(a)
# for i in range(len(ori)):
#     if ori[i] not in al:
#         al.append(ori[i])
# alpri=[0]*len(al)
# for j in range(len(al)):
#     for k in range(len(ori)):
#         if al[j]==ori[k]:
#             alpri[j]+=1
# m=0
# ok=0
# for l in range(len(al)):
#     if alpri[l]==max(alpri):
#         m=l
# for k in range(len(al)):
#     if alpri[k]==max(alpri):
#         ok+=1
# if ok>1:
#     print("?")
# else:
#     print(al[m])

a=input()
al=list(a)
di={}
for i in range(len(al)):
    if al[i] not in di:
        di[al[i]]=0
print(di)

for j in range(len(di)):
    for k in range(len(al)):
        if al[j]==di[k]:
            di[al[j]]+=1
print(di)
