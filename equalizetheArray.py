n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
flag = {}
maxl = 0
for i in xrange(n):
    if not flag.get(a[i]):
        flag[a[i]] = 1
    else:
        flag[a[i]]+=1
#ar_list = sorted(flag)
ar_list = [v[0] for v in sorted(flag.iteritems(), key=lambda(k, v): (v, k))]
#print ar_list, flag
min_num = 0
for i in xrange(len(ar_list)-1):
    min_num =min_num + flag[ar_list[i]]
print min_num