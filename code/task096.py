def p(a,t=range):
 d=[*{*sum(a,[])}];r=[[0,10,t]for t in d]
 for m in t(4):
  for u in a:
   for m in t(len(d)):
    q=[i for i in t(len(u))if u[i]==d[m]];e=o=0
    if q:e,o=min(q),max(q)
    if(o-e+1)>=r[m][0]:
      q=[i for i in t(e,o)if u[i]-d[m]];c=o-e+1
      if q:s=max(q)-min(q)+1;c=(min(q)-e)*2+s
      else:s=0
      if(r[m][1]>s)|(c>r[m][0]):r[m][1]=s;r[m][0]=c
  a=[*zip(*a[::-1])]
 r.sort();a=eval(str([[r[-1][2]]*r[-2][0]]*r[-2][0]))
 for m in t(4):
  for m in t(len(r)-1):u,s=r[m][:2];c,i=(u-s)//2,len(r)-m-2;a[i][i:i+u]=[r[m][2]]*c+[r[-1][2]]*s+[r[m][2]]*c if s else[r[m][2]]*u
  a=[*map(list,zip(*a[::-1]))]
 return a