def p(e):
 p,m=zip(*((p//10,p%10)for p in range(100)if e[p//10][p%10]))
 for s,t in zip(p,m):exec("a,b=max(p)-t+min(m),min(m)+s-min(p);e[s:=a][t:=b]=e[s][t];"*4)
 return e