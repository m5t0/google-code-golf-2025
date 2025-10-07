def p(g):r=range(l:=len(g));return[[g[i][j]*((i+j+1)%l>0<(i-j)%l)for j in r]for i in r]


def p(g):
 for i,v in enumerate(g):v[i]=v[~i]=0
 return g


p=lambda g:[exec("v[i]=v[~i]=0")for i,v in enumerate(g)]and g