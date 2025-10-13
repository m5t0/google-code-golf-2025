def p(o,n=range):
 l=len(o);r=1
 for x in n(4):
  e,i=zip(*((x,f)for x in n(l)for f in n(l)if o[x][f]));e,u,f,a=min(e),max(e),min(i),max(i);x=o[e][f];i=o[e].count(x)
  if(i<o[u].count(x))&r:
   r,i,j=0,f+i//2,a-i//2
   for x in n(u):o[x][i:j+1]=[4]*(j-i+1)
   for x in n(e+1,u):o[x][f+1:a]=[4]*(a-f-1)
   for f in n(e+1):
    if i>=f:o[e-f][i-f]=4
    if j+f<l:o[e-f][j+f]=4
  o=[*map(list,zip(*o[::-1]))]
 return o