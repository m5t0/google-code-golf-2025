def p(g,r=range):
 c=w=l=e=0;L=len(g);R=len(g[0])
 for I in r(L*R):
  if n:=g[i:=I//R][j:=I%R]:
   o=p=0
   while o+i<L and g[i+o][j]==n:o+=1
   while j+p<R and g[i][j+p]==n:p+=1
   if o*p>l*e:c,w,l,e=i,j,o,p
 return[[min(v:=sum(g,[]),key=v.count)*(g[c+i][w+j]>0)for j in r(e)]for i in r(l)]