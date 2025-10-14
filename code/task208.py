def p(r):
 t=sum(r,[]);q=r[t.index(m:=min(t,key=t.count))//21].count(m)-2;o=t.count(m)//2-q-2
 for t in range((21-o)*(21-q)):
  s,u=divmod(t,21-o)
  for t in(any(any(t[s:s+q])for t in r[u:u+o])<1)*r[u-1:u+o+1]:t[s-1:s+q+1]=[m]+[any(t[s:s+q])*m]*q+[m]
 return r