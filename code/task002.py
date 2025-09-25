def p(g,r=str.replace):
 for _ in(g:=r(str(g),*'04'))*4:*g,=zip(*eval(r(r(str(g),'0, 4','0,0'),'(4','(0'))[::-1])
 return g