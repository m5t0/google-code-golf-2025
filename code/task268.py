def p(e,l=range):
 c=len(e);o=1
 for t in l(4):
  a,n=zip(*((t,i)for t in l(c)for i in l(c)if e[t][i]));a,f,i,r=min(a),max(a),min(n),max(n);t=e[a][i];n=e[a].count(t)
  if(n<e[f].count(t))&o:
   o,n,u=0,i+n//2,r-n//2
   for t in l(f):e[t][n:u+1]=[4]*(u-n+1)
   for t in l(a+1,f):e[t][i+1:r]=[4]*(r-i-1)
   for i in l(a+1):
    if n>=i:e[a-i][n-i]=4
    if u+i<c:e[a-i][u+i]=4
  e=[*map(list,zip(*e[::-1]))]
 return e