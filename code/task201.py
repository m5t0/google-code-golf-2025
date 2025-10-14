def p(f):
 (l,g),d,d,(e,h),*i=[(e,h)for e in range(13)for h in range(13)if f[e][h]==4]
 for e in f[l:e+1]:i+=[e[g:h+1]];e[g:h+1]=[0]*(h-g+1)
 f=[[e[0]for e in zip(e,*f)if any(e)]for e in f if any(e)];return[i[0],*[[i[1][0]]+e[::1-2*(i[1][0]in[*zip(*f)][-1])]+[i[1][-1]]for e in f],i[-1]]