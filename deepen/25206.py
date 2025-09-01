#baekjoon deepen 25206 9/1
#20개의 과목 정보를 받은 후 if문을 이용해서 각 과목의 등급을 점수화시킨 후 계산하는 방식으로 구현
cr=0
gr=0
for _ in range(20):
    n,c,g=map(str, input().split())
    cr+=float(c)
    if g=="A+":
        gr+=4.5*float(c)
    elif g=="A0":
        gr+=4*float(c)
    elif g=="B+":
        gr+=3.5*float(c)
    elif g=="B0":
        gr+=3*float(c)
    elif g=="C+":
        gr+=2.5*float(c)
    elif g=="C0":
        gr+=2*float(c)
    elif g=="D+":
        gr+=1.5*float(c)
    elif g=="D0":
        gr+=1*float(c)
    elif g=="F":
        gr+=0
    elif g=="P":
        cr-=float(c)
print(f"{gr/cr:.5f}")

#다른 풀이
#등급과 해당 점수를 딕셔너리로 저장한 후 과목정보를 받은후 해당하는 등급을 딕셔너리 값과 비교해서 점수화시킨 후 계산하는 방식으로 구현
cr=0
gr=0
grade_cha={"A+":4.5,"A0":4,"B+":3.5,"B0":3,"C+":2.5,"C0":2,"D+":1.5,"D0":1,"F":0}
for _ in range(20):
    n,c,g=map(str, input().split())
    cr+=float(c)
    if g in grade_cha:
        gr+=grade_cha[g]*float(c)
    elif g=="P":
        cr-=float(c)
print(f"{gr/cr:.5f}")