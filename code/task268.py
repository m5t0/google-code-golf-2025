def p(o,z=range):
 l=len(o);q=1
 for x in z(4):
  e,i=zip(*((x,f)for x in z(l)for f in z(l)if o[x][f]));e,u,f,p=min(e),max(e),min(i),max(i);x=o[e][f];i=o[e].count(x)
  if(i<o[u].count(x))&q:
   q,i,c=0,f+i//2,p-i//2
   for x in z(u):o[x][i:c+1]=[4]*(c-i+1)
   for x in z(e+1,u):o[x][f+1:p]=[4]*(p-f-1)
   for f in z(e+1):
    if i>=f:o[e-f][i-f]=4
    if c+f<l:o[e-f][c+f]=4
  o=[*map(list,zip(*o[::-1]))]
 return o