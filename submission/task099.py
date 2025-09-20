def p(g,r=range):
 for l in 3,4,5:
  for k in r(5*(10-l)):
   if{*g[(i:=k//5+l+1)-1][(j:=k%5):j+5]+[*[*zip(*g)][j]][i-l:i]}=={1}:
    for m in r((l+1)*5):g[p][q]=g[p:=i-m//5-1][q:=j+m%5]or max(w*(w!=1)for v in g[i-l:i]for w in v[j:j+5])
 return g