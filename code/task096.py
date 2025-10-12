def p(u,h=range):
 t=[*{*sum(u,[])}];f=[[0,10,d]for d in t]
 for d in h(4):
  for v in u:
   for d in h(len(t)):
    b=[a for a in h(len(v))if v[a]==t[d]];s=a=0
    if b:s,a=min(b),max(b)
    if(a-s+1)>=f[d][0]:
      b=[a for a in h(s,a)if v[a]-t[d]];r=a-s+1
      if b:e=max(b)-min(b)+1;r=(min(b)-s)*2+e
      else:e=0
      if(f[d][1]>e)|(r>f[d][0]):f[d][1]=e;f[d][0]=r
  u=[*zip(*u[::-1])]
 f.sort();u=eval(str([[f[-1][2]]*f[-2][0]]*f[-2][0]))
 for d in h(4):
  for d in h(len(f)-1):s,e=f[d][:2];r,a=(s-e)//2,len(f)-d-2;u[a][a:a+s]=[f[d][2]]*r+[f[-1][2]]*e+[f[d][2]]*r if e else[f[d][2]]*s
  u=[*map(list,zip(*u[::-1]))]
 return u