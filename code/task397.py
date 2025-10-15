def p(g,I=81):
 while I:
  I-=1;j=I%9
  for k in[*range(len(s:={*g[i:=I//9][j:j+2],*g[i+1][j:j+2]}))]*min(s):g[i+2+k][j:j+2]=3,3
 return g