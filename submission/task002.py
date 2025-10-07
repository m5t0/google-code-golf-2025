def p(a,r=str.replace):
 a=r(str(a),'0','4')
 for _ in a*4:a=[*zip(*eval(r(r(str(a),'0, 4','0,0'),'(4','(0'))[::-1])]
 return a