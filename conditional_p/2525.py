#7/30
# h, m = map(int, input().split())
# t=int(input())
# if m>=t:
#     print(h, m-t)
# else:
#     if h==0:
#         print(23,60-(t-m))
#         if t>60:
#             a=int(t/60)
#             h=h-a
#             b=t%60
#             if h-a<0:
#                 c=a-h
#                 print(23-c,b)
#             if m>=b:
#                 print(h, b)
#             else:
#                 print(h-1, 60-(b-m))
#     else:
#         print(h-1, 60-(t-m))


def ad(h,m,t):
    if h==0:
        print(23,60-(t-m))
    else :
        print(23+h,t)
        


h, m = map(int, input().split())
t=int(input())
if m>=t:
    print(h, m-t)
else: 
    if t>60:
        a=int(t/60)
        h=h-a
        t=t%60
        if m>=t:
            print(h, t)
            if h<=0:
                ad(h,m,t)
            else:
                print(h-1, 60-(t-m))
    else:   
        print(h-1, 60-(t-m))
    