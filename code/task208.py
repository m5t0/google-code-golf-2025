def p(n):
 f=sum(n,[]);o=n[f.index(m:=min(f,key=f.count))//21].count(m)-2;e=f.count(m)//2-o-2
 for f in range((21-e)*(21-o)):
  x,d=divmod(f,21-e)
  for f in(any(any(f[x:x+o])for f in n[d:d+e])<1)*n[d-1:d+e+1]:f[x-1:x+o+1]=[m]+[any(f[x:x+o])*m]*o+[m]
 return n