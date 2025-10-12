def p(r):
 p=len;*n,=zip(*r);r=[n,r][f:=1in{p({*u})for u in n}];n=p(r[0]);t=[n*[0]for u in r]
 for u in range(p(r)*n):
  if(u:=(l:=r[i:=u//n])[g:=u%n])*(p({*[*zip(*r)][g]})<2):
   i=t[i];i[g]=u;i[g-1]=u*(u in l[:g])
   if g<n-1:i[g+1]=u*(u in l[g+1:])
 return([*zip(*t)],t)[f]