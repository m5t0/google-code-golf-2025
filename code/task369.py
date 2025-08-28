def p(g,r=range):
 d=0,1,0,-1;x=len(g);y=len(g[0]);f=lambda f,g,n,s:[(s.add((I,J)),f(f,g,(I,J),s))for i in r(4)if (0<=(I:=n[0]+d[i])<x)&(0<=(J:=n[1]+d[(i+1)%4])<y)and(g[I][J]==0and(I,J)not in s)]
 return [[[t:=g[i][j],(lambda s={(i,j)}:(f(f,g,(i,j),s),4-len(s))[1])()][t==0]for j in r(y)]for i in r(x)]
