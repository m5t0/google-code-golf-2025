s=lambda j,m:max(((r:=(str(j)[1::3])).rfind("8",0,m+k)-r.rfind("2",0,m+k))*(r.find("8",m+k)%(l:=1+len(j))-r.find("2",m+k)%l)for k in[0,1])>0
def p(b,e=enumerate):
 f=eval(str(b))
 r=set()
 for m,j in e(b):
  for p,d in e(zip(*b)):
   f[m][p]+=s(d,m)+s(j,p)
   if f[m][p]>8:
    f[m][p]=2
    for k in range(9):
     if k!=4:r.add((m-1+k//3,p-1+k%3))
 return[[((m,p)in r and 8)or(d[m]>0)*(d[m]//8*6+2)for p,d in e(zip(*f))]for m,j in e(f)]