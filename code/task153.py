e=enumerate
def f(h,a,i,j):
 f=1
 for s,v in e(a):
  for t,w in e(v):
   if w:
    if(x:=i+s)<3>(y:=j+t)and h[x][y]<1:h[x][y]=w
    else:f=0
 return f
def p(g,r=range):
 a,b=[z for c in r(1,10)if(z:=[[w[i]for w in zip(*g)if c in w]for i,v in e(g)if c in v])]
 for k in r(16):
  h=[[0]*3for _ in r(3)]
  if f(h,a,k//8,k//4%2)&f(h,b,k%4//2,k%2):return h