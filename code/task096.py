def p(e,o=range):
 u=[*{*sum(e,[])}];r=[[0,10,o]for o in u]
 for l in o(4):
  for n in e:
   for l in o(len(u)):
    i=[t for t in o(len(n))if n[t]==u[l]];s=p=0
    if i:s,p=min(i),max(i)
    if(p-s+1)>=r[l][0]:
      i=[t for t in o(s,p)if n[t]-u[l]];c=p-s+1
      if i:q=max(i)-min(i)+1;c=(min(i)-s)*2+q
      else:q=0
      if(r[l][1]>q)|(c>r[l][0]):r[l][1]=q;r[l][0]=c
  e=[*zip(*e[::-1])]
 r.sort();e=eval(str([[r[-1][2]]*r[-2][0]]*r[-2][0]))
 for l in o(4):
  for l in o(len(r)-1):a,q=r[l][:2];c,t=(a-q)//2,len(r)-l-2;e[t][t:t+a]=[r[l][2]]*c+[r[-1][2]]*q+[r[l][2]]*c if q else[r[l][2]]*a
  e=[*map(list,zip(*e[::-1]))]
 return e