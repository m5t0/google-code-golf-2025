def p(g,e=enumerate):g=[[max(w[i],w[~i],v[~j],g[~i][~j])for j,w in e(zip(*g))]for i,v in e(g)];return[[w[i]or sum(y&1and(19-x>y>x)*a[x-17]+(19-x<y<x)*a[x-2]for x,y,a in((i,j,v),(j,i,w)))for j,w in e(zip(*g))]for i,v in e(g)]

