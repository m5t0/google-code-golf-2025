def p(e,r=range(10)):
 p,m=zip(*((p,m)for p in r for m in r if e[p][m]))
 for s,t in zip(p,m):exec("a,b=max(p)-t+min(m),min(m)+s-min(p);e[a][b]=e[s][t];s,t=a,b;"*4)
 return e