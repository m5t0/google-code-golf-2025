def p(l):
 f=sum(l,[]);n=528-f[::-1].index(1);p=f.index(1);a=n//23-p//23+1;e=o=n%23-p%23+1;x=range(a*o)
 for u in range(9-1):
  for s in range(-9,23+1):
   for z in range(-9,23+1):
    for f,n in[*zip(range(a*o),x)]*all((23>s+n//o>-1<z+n%o<23)<1>=l[p//23+f//e][p%23+f%e]or(23>s+n//o>-1<z+n%o<23and(l[p//23+f//e][p%23+f%e]<3>l[s+n//o][z+n%o]or l[p//23+f//e][p%23+f%e]==l[s+n//o][z+n%o]))for f,n in zip(range(a*o),x)):
     if 23>s+n//o>-1<z+n%o<23:l[s+n//o][z+n%o]=l[p//23+f//e][p%23+f%e]
  x=[[o-1-s%o,s%o][u%4>2]*a+s//o for s in x];a,o=o,a
 return l