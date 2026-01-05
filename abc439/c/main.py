import math

n=int(input())
max=math.isqrt(n)+1

ans_dic={}

for i in range(1,max-1):
    for j in range(i+1,max):
        squared=i**2+j**2
        if squared>n:
            continue

        if ans_dic.get(squared) is None:
            ans_dic[squared]=True
        else:
            ans_dic[squared]=False

ans_list=[k for k in ans_dic if ans_dic[k] is True]
print(len(ans_list))
print(*sorted(ans_list))

