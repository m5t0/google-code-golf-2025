def p(s,r=range,e=enumerate):
 t,*f,a=sum(s,[]),10
 for i,m in e(s):
  if(5in m)>i/9<(0in m[(u:=m.index(5)+1):(n:=9-m[::-1].index(5))]):f+=[x for e in r(u,n)if t[x:=i*a+e]<1]
  else:[t==exec("t[a-e[0]+f[0]],t[a]=t[a],0")for e in[[i for i,m in e(t)if m==a]for a in r(a)]if[a-e[0]for a in e]==[a-f[0]for a in f]for a in e];f=[]
 return[t[i*a:][:a]for i in r(a)]