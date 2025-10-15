def p(r):
 (e,o),n,n,(f,q),*p=[(f,q)for f in range(13)for q in range(13)if r[f][q]==4]
 for f in r[e:f+1]:p+=[f[o:q+1]];f[o:q+1]=[0]*(q-o+1)
 r=[[f[0]for f in zip(f,*r)if any(f)]for f in r if any(f)];return[p[0],*[[p[1][0]]+f[::1-2*(p[1][0]in[*zip(*r)][-1])]+[p[1][-1]]for f in r],p[-1]]