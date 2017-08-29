__author__ = 'jnoor'
import math

n = int(raw_input())
for num in range(1,n+1):
    for base in 'dXob':
        width=len(str('{0:b}'.format(n)))
        print '{0:{width}{base}} '.format(num, base=base, width=width),
    print

# #print '{0:{w}{b}}'.format(5, b = 'o', w = 3)
# width=len(str('{0:{b}}'.format(5, b = 'b')))
# print width
#
# print bin()