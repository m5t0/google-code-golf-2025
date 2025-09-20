def p(g):
 def D(i,j,c):g[i][j]=2;x=i+d[c];y=j+d[c+1];D(i+d[e:=c^1],j+d[e+1],e)if c|(j<9>i>0and g[x][y])else 0>x or D(x,y,c)
 d=-1,0,1,0;[D(9,i,0)for i in range(10)if g[9][i]];return g