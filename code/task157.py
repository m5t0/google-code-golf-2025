def p(g,R=range):
 a,*p=sum(g,e:=[]),;n=[[]];r=15
 for i in R(16):
  if(5in a[i::r])>i/r:p+=[i]
  elif p:e+=[[n for n in R(150)if a[n]>4and n%r in p]];n,*p=[i+[n]for i in n for n in R(45)if 1>a[n]],
 for i in n:
  i=[any(n-i+e[0]in e*(6>i%r-n%r)for i,e in zip(i,e))|a[n]%5for n in R(150)]
  if all(i[:45])*(i.count(0)==a.count(0)):return[i[n*r:][:r]for n in R(10)]