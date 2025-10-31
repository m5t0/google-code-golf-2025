def p(l):
 y,x=divmod(sum(l,[]).index(4),11);a=y&3;b=x&3;t=[[x*(x==5)for x in r]for r in l]
 for r in 0,1,2:t[4*a+r][4*b:4*b+3]=l[y-a+r][x-b:][:3]
 return t