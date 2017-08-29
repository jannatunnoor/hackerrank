__author__ = 'jnoor'
s = raw_input()
st = ''
for i in s:
    if i.isupper():
        st+=i.lower()
    else:
        st+=i.upper()
print st
