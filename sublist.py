__author__ = 'jnoor'
n = int(raw_input())
ls = []
gdls = []
for i in xrange(n):
    name = raw_input()
    grade = float(raw_input())
    gdls.append(grade)
    ls.append([name,grade])
ls.sort(key = lambda x: x[1])
gdls = list(set(gdls))
gdls.sort()
name= []
for i in xrange(len(ls)):
    if ls[i][1] == gdls[1]:
        name.append(ls[i][0])

name.sort()
for i in name:
    print i