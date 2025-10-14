def p(d,t=range(10)):
 u=sum(d,[]).index(2);x=[(f-u//10,s-u%10)for f in t for s in t if d[f][s]&2]
 for u,e in(d[0][5:7]==[0,2])*x:d[1+u][8+e]=2
 for s in t:
  for f in t:
   for u,e in x*all(f+x<10>s+u>=d[f+x][s+u]<1for x,u in x):d[f+u][s+e]=2
 if d[5].count(2)>7:d[1][3:7]=[0]*4
 return d