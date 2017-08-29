
import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    flag = {}
    for i in xrange(n):
        if not flag.get(ar[i]):
            flag[ar[i]] = 1
        else:
            flag[ar[i]] += 1

    ar_list = sorted(flag)
    return flag[ar_list.pop()]

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)


