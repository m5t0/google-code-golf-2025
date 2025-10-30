def p(f,g=range):
 f=[[0]*32,*[[0,*z,0]for z in f],[0]*32];i=eval(str(f))
 for z in g(8):
  u=-1;f=[*zip(*f)][::-1];i=[*map(list,zip(*i))][::-1]
  while u<33:
   u+=1;e=u
   for t in g(33,u,-1):
    for l in g(20):
     for a in i[u+1:t-1]*(sum(sum(z[:-l-1])for z in f[u:t])<1):
      a[:-l-2]=[3]*(30-l);u=t
      for w in 3,4:a[-l-w]-=3*(i[e][-l-w]<i[e][27-l])
 return[z[1:-1]for z in i[1:-1]]