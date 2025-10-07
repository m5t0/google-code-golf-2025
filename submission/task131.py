def p(g):
 if(n:=len(h:=[*zip(*g)]))>9:return[*zip(*p(h))]
 k=h[0].index(2);a=min(v:=[i for i,v in enumerate(g)if(i-k)*any(v)]);b=max(v)+1;return p(g[::-1])[::-1]if b<k else g[:k+1]+g[a:b]+[[8]*n]+g[b:]+g[k+2:a]
 
 
 
 
def p(g):
 if(n:=len(h:=[*zip(*g)]))>9:return[*zip(*p(h))]
 if [*zip(*g)][0].index(3)>[*zip(*g)][0].index(2):return p([v[::-1]for v in g])
 k=h[0].index(2);a=min(v:=[i for i,v in enumerate(g)if(i-k)*any(v)]);b=max(v)+1;return p(g[::-1])[::-1]if b<k else g[:k+1]+g[a:b]+[[8]*n]+g[b:]+g[k+2:a]