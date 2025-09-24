def p(g,r=range):
 n=13;h={c:[(i//n,i%n)for i in r(169)if g[i//n][i%n]==c]for c in r(10)};f={c:((x,y),[(d,i-x,(j-y)*((-1)**(c+1)))for i,j in h[d]])for c in(2,3)for d in r(10)for x,y in h[c]if{(x+s//3-1,y+s%3-1)for s in r(9)if s!=4}&{*h[d]}}
 for c in f:
  for x,y in h[c]:
   for d,i,j in f[c][1]*((x,y)!=f[c][0]):g[i+x][j+y]=d
 return g