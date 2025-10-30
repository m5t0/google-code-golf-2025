def p(_):
 f,*n,p=sum(_,[]),10
 for s,r in enumerate(_):
  if(5in r)>s/9<(0in r[(_:=r.index(5)+1):(r:=9-r[::-1].index(5))]):n+=[n for e in range(_,r)if f[n:=s*p+e]<1]
  else:[f==exec("f[p-e[0]+n[0]],f[p]=f[p],0")for e in[[s for s,r in enumerate(f)if r==p]for p in range(p)]if[p-e[0]for p in e]==[p-n[0]for p in n]for p in e];n=[]
 return[f[s*p:][:p]for s in range(p)]