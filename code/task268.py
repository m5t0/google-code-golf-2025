def p(o,n=range):
 l=len(o);r=1
 for c in n(4):
  e,i=zip(*((c,f)for c in n(l)for f in n(l)if o[c][f]));e,u,f,a=min(e),max(e),min(i),max(i);c=o[e][f];i=o[e].count(c)
  if(i<o[u].count(c))&r:
   r,i,t=0,f+i//2,a-i//2
   for c in n(u):o[c][i:t+1]=[4]*(t-i+1)
   for c in n(e+1,u):o[c][f+1:a]=[4]*(a-f-1)
   for f in n(e+1):
    if i>=f:o[e-f][i-f]=4
    if t+f<l:o[e-f][t+f]=4
  o=[*map(list,zip(*o[::-1]))]
 return o