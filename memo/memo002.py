# 嘘解法によるコードだが実行時間が長いので没
def p(g):
 n,r,g=len(g),range,[[c+4*(c==0)for c in r]for r in g];g[0][0]=0
 for c in r(999):
  for i in r(n)[::(t:=(-1)**(c&1))]:
   for j in r(n)[::t]:
    for x, y in[(t,0),(0,t)]:
     if (0<=i+x<n)*(0<=j+y<n) and ((v:=g[i+x][j+y])!=3)*((w:=g[i][j])!=3):g[i+x][j+y]=min(v,w)
 return g

# 公開ノートブックベースのコード
def p(g):
 r,n=range,len(g);v=[[0]*n for _ in r(n)]
 def f(i,j):
  if(0<=i<n)*(0<=j<n)*(v[i][j]<1)*(g[i][j]==0):v[i][j]=1;[f(i+d,j+e)for d,e in[(1,0),(-1,0),(0,1),(0,-1)]]
 [f(i,0)or f(i,n-1)or f(0,i)or f(n-1,i)for i in r(n)];return[[4 if g[i][j]==0 and v[i][j]<1 else g[i][j]for j in r(n)]for i in r(n)]

e=enumerate
f=lambda g,w,i,j:3in{*w[i:]}&{*w[:i]}and 0not in(s:={(3in{*z[j:]}&{*z[:j]})and(z[j:].index(3)+z[j::-1].index(3))for z in g[i-w[i::-1].index(3)+1:i+w[i:].index(3)]})and len(s)==1
p=lambda g:[[w[i]or 4*f(g,[*w],i,j)*f([*zip(*g)],v,j,i)for j,w in e(zip(*g))]for i,v in e(g)]

from pprint import *

pprint(
    p(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 3, 0, 0, 0],
            [0, 3, 0, 3, 0, 0],
            [0, 0, 3, 0, 3, 0],
            [0, 0, 0, 3, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)
