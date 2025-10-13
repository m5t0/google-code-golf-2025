def p(n,q=range(10)):
 f=sum(n,[]).index(2);r=[(e-f//10,u-f%10)for e in q for u in q if n[e][u]&2]
 for f,i in(n[0][5:7]==[0,2])*r:n[1+f][8+i]=2
 for u in q:
  for e in q:
   for f,i in r*all(e+f<10>u+q>=n[e+f][u+q]<1for f,q in r):n[e+f][u+i]=2
 if n[5].count(2)>7:n[1][3:7]=[0]*4
 return n