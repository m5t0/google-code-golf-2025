n=zip;t=enumerate
def p(i):
 for r in 0,1:
  e=0
  for o,a in t(i):
   if(u:=min(a))==max(a)>0:
    e=e or [[0]*len(a)for r in i];e[o]=a
    for a,p in t(n(*i)):e[o+(u in p[o+1:])-(u in p[:o])][a]=u
  if e:return[e,[*map(list,n(*e))][::-1]][r]
  i=[*map(list,n(*i[::-1]))]