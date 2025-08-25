def p(g,r=range):
 w=[]
 for u in g:w=max([u[0]]+[u[j+1]for j in r(len(u)-1)if u[j]-u[j+1]],w,key=len);s=len(w)
 return[[w[min(i,j,s-j-1,s-i-1)]for i in r(s)]for j in r(s)]