def p(g):
 if(n:=len(g))<3:return[[3]*n]*n
 if n<4:return[[3]*3,[0,0,3],[3]*3]
 e=[[3]*n,[0]*(n-1)+[3]]+[[3,0]+e+[0,3]for e in p([e[2:-2]for e in g[2:-2]])]+[[3]+[0]*(n-2)+[3],[3]*n];e[2][1]=3;return e