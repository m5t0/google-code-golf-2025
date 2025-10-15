def p(n):
 o=sum(n,[]);f=n[o.index(e:=min(o,key=o.count))//21].count(e)-2;y=o.count(e)//2-f-2
 for o in range((21-y)*(21-f)):
  d,k=divmod(o,21-y)
  for o in(any(any(o[d:d+f])for o in n[k:k+y])<1)*n[k-1:k+y+1]:o[d-1:d+f+1]=[e]+[any(o[d:d+f])*e]*f+[e]
 return n