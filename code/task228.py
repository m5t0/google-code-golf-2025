def f(t):e=[t for(t,e)in enumerate(t)if any(e)];return e[0],e[-1]
def p(t):
 e,i=f(t);p,r=f(zip(*t))
 def z(z,p,f,i):t[z][p],t[f][i]=t[f][i],t[z][p]
 z(e+1,p+1,i+1,r+1);z(e+1,r-1,i+1,p-1);z(i-1,p+1,e-1,r+1);z(i-1,r-1,e-1,p-1);return t