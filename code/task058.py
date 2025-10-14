def p(y):
 if(f:=len(y))<3:return[[3]*f]*f
 if f<4:return[[3]*3,[0,0,3],[3]*3]
 f=[[3]*f,[0]*(f-1)+[3]]+[[3,0]+f+[0,3]for f in p([f[2:-2]for f in y[2:-2]])]+[[3]+[0]*(f-2)+[3],[3]*f];f[2][1]=3;return f