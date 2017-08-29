__author__ = 'jnoor'
x=2;y=2;z=1
N = 2
ls = [[0,0,0],[x,0,0],[x,y,0],[0,y,0],[0,y,z],[0,0,z],[x,0,z],[x,y,z]]
print ls
#nwl = [x for x in ls if sum(x)!= N]
nwl = [[a,b,0] for a in xrange(x+1) for b in xrange(y+1)]
print nwl
#int(raw_input())


