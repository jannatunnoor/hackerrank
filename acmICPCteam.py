"""


"""

import sys
import time

# n,m = raw_input().strip().split(' ')
# n,m = [int(n),int(m)]
# topic = []
# for topic_i in xrange(n):
#    topic_t = str(raw_input().strip())
#    topic.append((topic_t))

n,m = 4,5
topic = ['10101','11100','11010','00101']

start = time.time()
max_topic_list = [bin(int(topic[i],2)|int(topic[j],2)).count('1') for i in xrange(n-1) for j in xrange(i+1,n)]
max = max(max_topic_list)
print max, '\n', max_topic_list.count(max)
end = time.time()
print 'minimal', (end-start)*1000


def setOfTopic(str):
    setT = []
    for i in xrange(1,m+1):
        if int(str[i-1]) & 1 == 1:
            setT.append(i)
    return set(setT)

start = time.time()
topicSet = [setOfTopic(i) for i in topic]
maximal_topic = 0
maximal_topic_team = 0
topic_team_dict = {}
for i in xrange(n-1):
    for j in xrange(i+1, n):
        topic_union = len(topicSet[i].union(topicSet[j]))
        if not topic_team_dict.get(topic_union):
            topic_team_dict[topic_union] = 1
        else:
            topic_team_dict[topic_union] += 1
lst = sorted(topic_team_dict, reverse = True)
print lst[0]
print topic_team_dict[lst[0]]
end = time.time()
print 'maximal', (end-start)*1000