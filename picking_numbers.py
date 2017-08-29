import sys

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
flag = {}
maxl = 0
for i in xrange(n):
    if not flag.get(a[i]):
        flag[a[i]] = 1
    else:
        flag[a[i]]+=1

ar_list = sorted(flag)
for i in xrange(len(ar_list)):
    count = flag[ar_list[i]]
    if count > maxl:
        maxl = count
    if i!=len(ar_list)-1:
        if abs(ar_list[i]-ar_list[i+1])<=1:
            count = flag[ar_list[i]]+ flag[ar_list[i+1]]
            if count > maxl:
                maxl = count

#print ar_list
#print flag
print maxl

