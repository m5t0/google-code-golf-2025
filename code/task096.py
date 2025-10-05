def p(g,r=range):
 c=[i for i in r(10)if i in sum(g,[])];f=[[0,10,t]for t in c]
 for _ in r(4):
  for v in g:
   for i in r(len(c)):
    a=[j for j in r(len(v))if v[j]==c[i]];s=l=0
    if a:s,l=min(a),max(a)
    if(l-s+1)>=f[i][0]:
      b=[j for j in r(s,l+1)if v[j]!=c[i]];X=l-s+1
      if b==[]:x=0
      else:x=max(b)-min(b)+1;X=(min(b)-s)*2+x
      if(f[i][1]>x)|(X>f[i][0]):f[i][1]=x;f[i][0]=X
  g=[*map(list,zip(*g[::-1]))]
 f.sort();g=eval(str([[f[-1][2]]*f[-2][0]]*f[-2][0]))
 for _ in r(4):
  for i in r(len(f)-1):w,x=f[i][:2];X,j=(w-x)//2,len(f)-i-2;g[j][j:j+w]=[f[i][2]]*X+[f[-1][2]]*x+[f[i][2]]*X if x else[f[i][2]]*w
  g=[*map(list,zip(*g[::-1]))]
 return g