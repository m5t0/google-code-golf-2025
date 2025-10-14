n=zip;m=enumerate
def p(i):
 for r in 0,1:
  e=0
  for o,f in m(i):
   if(u:=min(f))==max(f)>0:
    e=e or [[0]*len(f)for r in i];e[o]=f
    for f,p in m(n(*i)):e[o+(u in p[o+1:])-(u in p[:o])][f]=u
  if e:return[e,[*map(list,n(*e))][::-1]][r]
  i=[*map(list,n(*i[::-1]))]