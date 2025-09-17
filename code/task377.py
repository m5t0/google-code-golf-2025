def p(g,r=range,w=()):
 for u in g:w=max(u[:1]+[u[j+1]for j in r(len(u)-1)if u[j]-u[j+1]],w,key=len);s=len(w)
 return[[w[min(i,j,s+~j,s+~i)]for i in r(s)]for j in r(s)]