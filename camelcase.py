s = raw_input().strip()
count = 1
for i in xrange(len(s)):
    if s[i].isupper():
        count+=1
print count

