def p(g,r=range):
 l=len({*g[4]})+1;t=r(l*5);h=[[g[i//l][j//l]for j in t]for i in t];t=h[:-l];f=lambda k=min,t=[*zip(*h)][:-l]:k(i for i,v in enumerate(t)if any(v[:-l]));a=f(t=t),f(max,t);b=f(),f(max)
 for s in r(4):
  x=s//2*2-1;y=s%2*2-1;p=a[s//2];q=b[s%2]
  while h[p+x][q+y]<1:p+=x;q+=y;h[p][q]=2
 return h