n=zip;u=enumerate
def p(e):
 for z in 0,1:
  i=0
  for r,l in u(e):
   if(f:=min(l))==max(l)>0:
    i=i or [[0]*len(l)for z in e];i[r]=l
    for l,m in u(n(*e)):i[r+(f in m[r+1:])-(f in m[:r])][l]=f
  if i:return[i,[*map(list,n(*i))][::-1]][z]
  e=[*map(list,n(*e[::-1]))]