def p(g,r=range,L=len):
 n=L(g[0]);z=[((k-i+1)*(d:=l-j+1),i,j,d)for i in r(L(g))for j in r(n)for k in r(i,L(g))for l in r(j,n)if max(max(v[j:l+1])for v in g[i:k+1])<1and{*sum([*zip(*g[i-1:i]+g[k+1:k+2])][j:l+1]+(z:=[*zip(*g[i:k+1])])[j-1:j]+z[l+1:l+2],())}=={2}]
 for v,i,j,d in z:
  for k in r(v):g[i+k//d][j+k%d]=8*(v==min(z)[0])+(v==max(z)[0])
 return g