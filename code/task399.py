def p(g,r=range(3)):
 return [[(~(k:=3*i+j)%2&(sum(x!=0for a in g for x in a)//2>k))for j in r]for i in r]