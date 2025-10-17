#baekjoon mutiple and divisor 2501 10/17
#두 변수를 받고 약수 맞으면 n값을 증가 시키면서 b와 같을 때 found를 True로 만들어서 프로그램을 멈추고 못 찾을 시 0을 출력하는 방식으로 구현
a, b = map(int, input().split())
n= 0
found = False
for i in range(1, a + 1):
    if a % i == 0:
        n += 1 
    if n== b:
        print(i)      
        found = True  
        break         
if not found:
    print(0)       
