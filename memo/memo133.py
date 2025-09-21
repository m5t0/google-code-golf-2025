def p(g,r=range):
 a=sum(g,[]);m=len(a);n,*l=len(g[0]),
 for i in r(m):
  if a[i]and(str(i)in str(l))<1:
   v={i}
   for _ in r(50):v|={j+x for j in v for x in(-n,-1,1,n)if(x%n<1or j//n==(j+x)//n)and j+x<m and a[j+x]}
   l+=[(max(k for k in r(1,5)if(t:={min(v)+i//k+i%k*n for i in r(k*k)})<v and len({a[l]for l in t})<2),-len(v),[*v])]
 (A,B,b),*l=sorted(l)
 for A,B,v in l:
  x,y,c=min((x,y,a[x])for x in v for y in b if a[x]==a[y])
  for i in b:
   for j in r(A*A):g[x//n+A*(i//n-y//n)+j//A][x%n+A*(i%n-y%n)+j%A]=(a[i]>0)*[max(a[k]for k in v if a[k]!=c),c][a[i]==c]
 return g

def p(u):
 # eは色がついている座標とその色を持つ辞書
 e,t,*o={(p,m):v for p,u in enumerate(u)for m,v in enumerate(u)if v},[]
 # 隣り合う色がついたマスを取ってくる関数
 def p(u):
  if u in e:r[u]=e.pop(u);p((u[0]-1,u[1]));p((u[0]+1,u[1]));p((u[0],u[1]-1));p((u[0],u[1]+1))
 # oにブロックごとの辞書を持つ
 while e:o+=[r:={}];p(min(e))
 # ブロックごとにループを回す
 for r in o+o:
  # iは特徴点の色、gは特徴点以外の色, (p,m)は特徴点の座標；iはブロック内のグリッドサイズ、tはブロックサイズが1の場合の特徴点からの相対座標のリスト(特徴点は除く)
  i,={*o[0].values()}&{*o[1].values()};g,={*r.values()}-{i};p,m=min(e:=[u for u in r if r[u]==i]);i=max(e)[0]+1-p;t+=[(u[0]-p,u[1]-m)for u in r if(r[u]==g)==i]
  # 相対座標に基づいて更新
  for r,v in t:
   for e in range(i*i):u[p+r*i+e//i][m+v*i+e%i]=g
 return u