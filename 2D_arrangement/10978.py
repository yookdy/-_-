#baekjoon twodimensional ordering 10978 9/3~9/4
#2차원 리스트를 받는데 각 행의 길이가 다를 수 있기에 최대 길이를 구하고 그 길이만큼 
# for문을 이용해서 각 행의 길이를 비교해서 인덱스가 존재하면 pr리스트에 추가하는 방식으로 구현
li=[]
for _ in range(5):                
    line=input().strip()
    li.append(line)
pr=[]
m=0                        
for row in li:
    if len(row)>m:
        m=len(row)
for j in range(m):           
    for i in range(5):             
        if j<len(li[i]):         
            pr.append(li[i][j])
print("".join(pr))               
