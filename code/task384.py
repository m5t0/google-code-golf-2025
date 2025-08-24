def p(g,e=enumerate,r=range):
 a,b=min(s:=[i for r in g for i,x in e(r)if x>0]),max(s)
 c,d=min(t:=[i for j in zip(*g) for i,x in e(j) if x>0]),max(t)
 return[[g[j//2+c][i//2+a]for i in r(2*(b-a+1))]for j in r(2*(d-c+1))]