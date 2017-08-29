import sys

arr = map(int, raw_input().strip().split(' '))
min = max = 0
for i in xrange(len(arr)-1):
    min = min + arr[i]
max = min
for i in xrange(len(arr)-1):
    sum = 0
    for j in xrange(len(arr)):
        if i !=j:
            sum = sum + arr[j]

    if sum < min:
        min = sum
    if sum > max:
        max = sum
print min, '', max