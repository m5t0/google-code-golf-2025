r=range(841)
def p(n):
 for f in r:
  i,d=f//56+1,f//2%28+1;t=r[:29];g,p=[d*[0]for f in t],1
  for x in r:m=n[q:=x//29][a:=x%29];e=g[x:=(q-f%2*a//6)%i][a%d];p-=m*e*(m!=e);g[x][a%d]=max(m,e)
  if p>0:return[[g[(x-f%2*a//6)%i][a%d]for a in t]for x in t]