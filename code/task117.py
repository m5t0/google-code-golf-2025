def p(a,f=enumerate):
 n,t=[(i,p)for i,r in f(a)for p,r in f(r)if r*(p<len(a)-3>i>3)and all(a[i+n//3][p+n%3]==r*(1-(n//3+n%3)%2)for n in range(9))][0]
 for i,r in f(a):
  for p,r in f(r):
   if r and r-a[n][t]:a[o:=2*n-i+2][p]=a[i][p:=2*t-p+2]=a[o][p]=r
 return a