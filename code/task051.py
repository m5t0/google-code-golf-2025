def p(f,r=range):
 s=sum(f,[]);u,t=divmod(s.index(min(s,key=s.count)),i:=len(f[0]))
 for l in r(9):
  if(n:=l//3-1,l:=l%3-1)!=(0,0)and n*l==0and f[u-n][t-l]<1:return[[f[s][o]or((s-u)*l==(o-t)*n and(n and(s-u)//n>0 or l and(o-t)//l>0))*f[u][t]for o in r(i)]for s in r(len(f))]