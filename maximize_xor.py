def maxXor(l, r):
    if l==r:
        return 0
    max = 0
    for i in xrange(l,r):
        for j in xrange(i+1,r+1):
            x = i^j
            if x>max:
                max = x
    return max


_l = int(raw_input())
_r = int(raw_input())

res = maxXor(_l, _r)
print(res)