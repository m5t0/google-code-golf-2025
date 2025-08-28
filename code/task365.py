def p(g,r=range):
 I=J=p=u=e=0
 for i in r(len(g)):
  for j in r(len(g[0])):
   c=d=f=0
   while i+c<len(g)and g[i+c][j]:c+=1
   while j+d<len(g[0])and g[i][j+d]:d+=1
   f=sum(g[i+k][j+l]==2for k in r(c)for l in r(d))
   if f>e:I=i;J=j;p=c;u=d;e=f
 return[[g[i+I][j+J]for j in r(u)]for i in r(p)]