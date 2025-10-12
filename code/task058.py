def p(f):
 if(g:=len(f))<3:return[[3]*g]*g
 if g<4:return[[3]*3,[0,0,3],[3]*3]
 i=[[3]*g,[0]*(g-1)+[3]]+[[3,0]+o+[0,3]for o in p([o[2:-2]for o in f[2:-2]])]+[[3]+[0]*(g-2)+[3],[3]*g];i[2][1]=3;return i