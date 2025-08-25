def p(g):
 for c in range(1,10):
  h=[[q*(q==c)for q in p]for p in g]
  if(x:=[[v[j]for j in range(30)if any([*zip(*h)][j])]for v in h if any(v)])and sum(map(sum,x))//c>len(x)*len(x[0])//2:return x