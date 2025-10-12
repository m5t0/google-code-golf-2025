def p(t,e=enumerate):
 n,f=[(i,b)for i,r in e(t)for b,r in e(r)if r*(b<len(t)-3>i>3)and all(t[i+n//3][b+n%3]==r*(1-(n//3+n%3)%2)for n in range(9))][0]
 for i,r in e(t):
  for b,r in e(r):
   if r and r-t[n][f]:t[l:=2*n-i+2][b]=t[i][b:=2*f-b+2]=t[l][b]=r
 return t