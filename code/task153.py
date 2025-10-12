r=enumerate
def y(i,e,a,u):
 y=1
 for g,e in r(e):
  for e,f in r(e):
   if f:
    if(p:=a+g)<3>(n:=u+e)and i[p][n]<1:i[p][n]=f
    else:y=0
 return y
def p(g,f=range(16)):
 e,u=[p for u in f[1:]if(p:=[[f[a]for f in zip(*g)if u in f]for a,e in r(g)if u in e])]
 for g in f:
  i=[[0]*3for y in f[:3]]
  if y(i,e,g//8,g//4%2)&y(i,u,g%4//2,g%2):return i