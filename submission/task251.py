def p(g,r=str.replace):
 for _ in(g:=r(str(g),*'01'))*4:*g,=zip(*eval(r(r(str(g),'0, 1','0,0'),'(1','(0'))[::-1])
 return g