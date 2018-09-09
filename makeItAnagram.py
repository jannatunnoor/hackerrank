"""
Problem: https://www.hackerrank.com/challenges/make-it-anagram-mglines/problem
"""

w1 = raw_input()
w2= raw_input()
total=0
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter in w1 and letter in w2:
        total += abs(w1.count(letter)-w2.count(letter))
    else:
        for x in [w1,w2]:
            if letter in x:
                total+=x.count(letter)
print total