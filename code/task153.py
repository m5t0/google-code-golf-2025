e=enumerate
def d(h,t,i,z):
 d=1
 for s,t in e(t):
  for t,l in e(t):
   if l:
    if(o:=i+s)<3>(n:=z+t)and h[o][n]<1:h[o][n]=l
    else:d=0
 return d
def p(g,r=range(16)):
 t,x=[p for x in r[1:]if(p:=[[l[i]for l in zip(*g)if x in l]for i,t in e(g)if x in t])]
 for s in r:
  h=[[0]*3for d in r[:3]]
  if d(h,t,s//8,s//4%2)&d(h,x,s%4//2,s%2):return h