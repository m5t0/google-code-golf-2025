def p(g):
 g=g[0]
 s=5*sum(x!=0 for x in g)
 g=[0]*s+g+[0]*s
 r=range(s) 
 return[[g[i+j+1]for j in r]for i in r]