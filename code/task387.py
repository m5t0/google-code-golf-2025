def p(g,r=range):
 a=[[i,j]for i in r(len(g))for j in r(len(g[0]))if g[i][j]>0];X,Y=zip(*a);m,k,l,o=min(X),max(X),min(Y),max(Y)
 for i in r(len(g)):
  for j in r(len(g[0])):
   (x,y),d=min(((p,max(abs(i-p[0]),abs(j-p[1])))for p in a),key=lambda t:t[1])
   g[i][j]=[[g[i][j],[v for v in g[x] if 0<v!=g[x][y]][0]][0<d<2],5][(~min(j-l,o-j)&1)*(i in X)*(l<j<o)|((~min(i-m,k-i)&1)*(j in Y)*(m<i<k))]
 return g