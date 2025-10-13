def p(r):
 (g,i),t,t,(s,e),*h=[(h,d)for h in range(13)for d in range(13)if r[h][d]==4]
 for d in r[g:s+1]:h+=[d[i:e+1]];d[i:e+1]=[0]*(e-i+1)
 g=[[h[0]for h in zip(d,*r)if any(h)]for d in r if any(d)];return[h[0],*[[h[1][0]]+d[::1-2*(h[1][0]in[*zip(*g)][-1])]+[h[1][-1]]for d in g],h[-1]]