def p(g):
 if(n:=len(g))<3:return[[3]*n]*n
 if n==3:return[[3]*3,[0]*2+[3],[3]*3]
 a=[[3]*n,[0]*(n-1)+[3]]+[[3,0]+v+[0,3]for v in p([s[2:-2]for s in g[2:-2]])]+[[3]+[0]*(n-2)+[3],[3]*n];a[2][1]=3;return a