def p(g,e=enumerate):
 i,j=min((i,j)for i,v in e(g)for j,w in e(v)if len(s:={*sum((a[j:j+3]for a in g[i:i+3]),[])})>1>(0in s));d,*l=3+(g[i][j+3]>0),
 for v in g[i:i+d]:l+=[v[j:j+d]];v[j:j+d]=[0]*d
 n=len(h:=[[w[0]for w in zip(v,*g)if any(w)]for v in g if any(v)]);m=n//d;return[[w*(h[m*i][m*j]>0)for j,w in e(v)]for i,v in e(l)]