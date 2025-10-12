def p(i,y=range):
 t=[*{*sum(i,[])}];f=[[0,10,r]for r in t]
 for r in y(4):
  for v in i:
   for r in y(len(t)):
    g=[a for a in y(len(v))if v[a]==t[r]];s=a=0
    if g:s,a=min(g),max(g)
    if(a-s+1)>=f[r][0]:
      g=[a for a in y(s,a)if v[a]-t[r]];m=a-s+1
      if g:e=max(g)-min(g)+1;m=(min(g)-s)*2+e
      else:e=0
      if(f[r][1]>e)|(m>f[r][0]):f[r][1]=e;f[r][0]=m
  i=[*zip(*i[::-1])]
 f.sort();i=eval(str([[f[-1][2]]*f[-2][0]]*f[-2][0]))
 for r in y(4):
  for r in y(len(f)-1):s,e=f[r][:2];m,a=(s-e)//2,len(f)-r-2;i[a][a:a+s]=[f[r][2]]*m+[f[-1][2]]*e+[f[r][2]]*m if e else[f[r][2]]*s
  i=[*map(list,zip(*i[::-1]))]
 return i