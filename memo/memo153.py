f=lambda a,i,j,s,t:len(a)>s-i>-1<t-j<len(a[0])and a[s-i][t-j]
def p(g,r=range,e=enumerate):
 a,b=[z for c in r(1,10)if(z:=[[w[i]for w in zip(*g)if c in w]for i,v in e(g)if c in v])]
 for k in r(16):
  if max((i:=k//8)+len(a),(j:=k//4%2)+len(a[0]),(x:=k%4//2)+len(b),(y:=k%2)+len(b[0]))<4and min(sum((h:=[[[0,(v:=f(a,i,j,s,t)),(w:=f(b,x,y,s,t)),-1][(v>0)+2*(w>0)]for t in r(3)]for s in r(3)]),[]))>-1:return h

e=enumerate
f=lambda h,a,i,j:[exec("h[x][y]="+["-1","w"][h[x][y]<1])for s,v in e(a)for t,w in e(v)if((x:=i+s)<3>(y:=j+t))*w]and"-1"not in str(h)and j+len(a[0])
def p(g,r=range):
 a,b=[z for c in r(1,10)if(z:=[[w[i]for w in zip(*g)if c in w]for i,v in e(g)if c in v])]
 for k in r(16):
  h=[[0]*3for _ in r(3)]
  if f(h,a,k//8,k//4%2)&f(h,b,k%4//2,k%2):return h