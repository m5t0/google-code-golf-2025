def p(e,p=enumerate):
 m,r=[(u,n)for u,n in p(e)for n,a in p(n)if a*(n<len(e)-3>u>3)and all(e[u+m//3][n+m%3]==a*(1-(m//3+m%3)%2)for m in range(9))][0]
 for u,a in p(e):
  for n,a in p(a):
   if a and a-e[m][r]:e[a:=2*m-u+2][n]=e[u][n:=2*r-n+2]=e[a][n]=a
 return e