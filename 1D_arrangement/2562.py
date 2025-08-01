list1 = [int(input()) for _ in range(9)]
a=max(list1)
print(a)
for i in range(len(list1)):
    if list1[i]==a:
        print(i+1)