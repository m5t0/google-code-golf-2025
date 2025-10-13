def p(r):
 p=len;*n,=zip(*r);r=[n,r][f:=1in{p({*o})for o in n}];n=p(r[0]);t=[n*[0]for o in r]
 for o in range(p(r)*n):
  if(o:=(e:=r[i:=o//n])[a:=o%n])*(p({*[*zip(*r)][a]})<2):
   i=t[i];i[a]=o;i[a-1]=o*(o in e[:a])
   if a<n-1:i[a+1]=o*(o in e[a+1:])
 return([*zip(*t)],t)[f]