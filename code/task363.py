def p(f):
 c=sum(f,[]).index(2);_=[(d-c//10,e-c%10)for d in range(10) for e in range(10) if f[d][e]&2]
 for c,o in(f[0][5:7]==[0,2])*_:f[1+c][8+o]=2
 for e in range(10):
  for d in range(10):
   for c,o in _*all(d+c<10>e+o>=f[d+c][e+o]<1for c,o in _):f[d+c][e+o]=2
 if f[5].count(2)>7:f[1][3:7]=[0]*4
 return f