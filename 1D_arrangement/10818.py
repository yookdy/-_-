#baekjoon one dimensional ordering 10818
#파이썬 내장함수를 이용해서 최대, 최소를 구하는 방식으로 구현
a=int(input())
list1 = [int(x) for x in input().split()]#메서드 이용 split()--빈칸으로 니누기
max= max(list1)
min= min(list1)
print(min,max)