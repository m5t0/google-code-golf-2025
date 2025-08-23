def p(g,r=range):
 d={}
 for v in g:
  for x in v:d[x]=d.get(x,0)+1
 s=min(d,key=d.get)
 c=w=l=e=0
 for i in r(L:=len(g)):
  for j in r(R:=len(g[0])):
   if (n:=g[i][j])>0!=n-s:
    o=p=0
    while o+i<L and g[i+o][j]==n:o+=1
    while j+p<R and g[i][j+p]==n:p+=1
    if o*p>l*e:c,w,l,e=i,j,o,p
 return[[[0,s][g[c+i][w+j]>0]for j in r(e)]for i in r(l)]