def p(g):
 n=len(g[0]);f=sum(g,[]);k=[i for i,x in enumerate(f)if x%5];j=min(i%n for i in k);b=f.index(5)-k[0]+k[0]%n-j+~n
 for i in k:g[(b+i)//n][(b+i)%n]=f[i]
 return g