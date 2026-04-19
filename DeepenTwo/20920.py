# baekjoon DeepTwo 20920 26/04/19
# 처음 입력값을 받고 길이 조건에 맞는 걸 거르고 중복성, 문자 길이, 말파벳 순으로 소팅하는 과정을 거치면서 출력하는 방식으로 구현
# 처음 코드에서는 시간 초과로 인해서 import sys를 추가해서 속도 개선
import sys

input = sys.stdin.read().split()

n = int(input[0])
m = int(input[1])
words = input[2:]

dic = {}

for word in words:
    if len(word) >= m:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

sorted_words = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word, count in sorted_words:
    print(word)
