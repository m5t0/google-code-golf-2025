def p(g,r=range):
 a=g[0][0];l=sorted((sum(g,[]).count(i),i)for i in r(10)if i!=a);b=l[-1][1];c=[i for _,i in l if f'{i}, {b}'in str(g) and i!=b][0]
 for i in r(900):
  if g[i//30][i%30]==c:
   f=[v[i%30-1:i%30+2]for v in g[i//30-1:i//30+2]]
   if(b in sum(f,[])or a==f[0][1])^1:
    p=[v[i%30-1:i%30+2]for v in g[i//30-1:i//30+2]]
    for k in r(25):g[i//30-2+k//5][i%30-2+k%5]=a
 p=eval(str(p).replace(str(a),str(b)));f=eval(str(g))
 for i in r(900):
  for k in r((g[i//30][i%30]==c)*9):f[i//30-1+k//3][i%30-1+k%3]=p[k//3][k%3]
 a=p[0][1]if p[0][1]!=p[0][0]else p[1][0];exec(f"f[:]=zip(*eval(str(f).replace('{c}, {a}, {b}','{c},{a},{a}').replace('{a}, {a}, {b}','{a},{a},{a}'))[::-1]);"*60);return f