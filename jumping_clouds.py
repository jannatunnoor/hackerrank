import sys

n = int(raw_input().strip())
c = map(int, raw_input().strip().split(' '))
jump = 0
i = 0
while i <= n - 2:
    if i+2 <n and c[i + 2] == 0:
        jump += 1
        i+=2
    else:
        if c[i + 1] == 0:
            jump += 1
        i+=1

print jump
