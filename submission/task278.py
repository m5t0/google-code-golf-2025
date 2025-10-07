def p(g,r=range):n=len(g);m=len(g[0]);f=lambda i,j:sum((n>i+k>=0and g[i+k][j])+(m>j+k>=0and g[i][j+k])for k in[-1,1]);s={(i-1+k//3,j-1+k%3)for k in r(9)for i in r(n)for j in r(m)if g[i][j]&f(i,j)};return[[g[i][j]or((i,j)in s)*3for j in r(m)]for i in r(n)]

def p(a):
 for _ in a:a=[*zip(*eval(str(a).replace('0, 2, 2','3,2,2'))[::-1])]
 return a