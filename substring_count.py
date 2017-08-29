__author__ = 'jnoor'
s = raw_input()
# subst = raw_input()
# c=0
# for i in xrange(len(st)-len(subst) + 1):
#     if st[i:(len(subst)+i)] == subst:
#         c+=1
# print c
# print True if s.isalnum() else False
# print True if s.isalpha() else False
# print True if s.isdigit() else False
# print True if s.islower() else False
# print True if s.isupper() else False

print True if any([i.isalnum() for i in s ]) == True else False
print True if any([i.isalpha() for i in s ]) == True else False
print True if any([i.isdigit() for i in s ]) == True else False
print True if any([i.islower() for i in s ]) == True else False
print True if any([i.isupper() for i in s ]) == True else False