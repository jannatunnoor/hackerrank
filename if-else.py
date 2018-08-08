"""
Problem description: https://www.hackerrank.com/challenges/py-if-else/problem
"""
#
#solution no 1
N = int(raw_input())
if N & 1:
    print 'Weird'
else:
    if N >= 6 and N <= 20:
        print 'Weird'
    elif N > 20 or (N >= 2 and N <= 5):
        print 'Not Weird'

#solution no 2
n = int(raw_input().strip())
if n&1==0 and (n in range(2,6) or n>20):
    print 'Not Weird'
else:
    print 'Weird'

#solution no 3 without if condition
n = int(raw_input().strip())
check = {1: 'Not Weird', 0: 'Weird'}
print check[n&1==0 and (n in range(2,6) or n>20)]
