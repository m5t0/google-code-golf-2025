def p(g):
 d={}
 for r in g:
  for x in r:
   d[x]=d.get(x,0)+1
 return [[x]for x in sorted(d,key=d.get,reverse=1)[2:5]]