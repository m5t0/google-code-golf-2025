def p(g):
 (h,o),d,d,(e,j),*z=[(p,j)for p in range(13)for j in range(13)if g[p][j]==4]
 for p in g[h:e+1]:z+=[p[o:j+1]];p[o:j+1]=[0]*(j-o+1)
 g=[[p[0]for p in zip(p,*g)if any(p)]for p in g if any(p)];return[z[0],*[[z[1][0]]+p[::1-2*(z[1][0]in[*zip(*g)][-1])]+[z[1][-1]]for p in g],z[-1]]