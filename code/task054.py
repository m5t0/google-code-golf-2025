def p(g,d=range):
 a=g[0][0];i=sorted((sum(g,[]).count(e),e)for e in d(10)if e!=a);s=i[-1][1];t=[e for _,e in i if f'{e}, {s}'in str(g) and e!=s][0]
 for e in d(900):
  if g[e//30][e%30]==t:
   f=[v[e%30-1:e%30+2]for v in g[e//30-1:e//30+2]]
   if(s in sum(f,[])or a==f[0][1])^1:
    p=[v[e%30-1:e%30+2]for v in g[e//30-1:e//30+2]]
    for k in d(25):g[e//30-2+k//5][e%30-2+k%5]=a
 p=eval(str(p).replace(str(a),str(s)));f=eval(str(g))
 for e in d(900):
  for k in d((g[e//30][e%30]==t)*9):f[e//30-1+k//3][e%30-1+k%3]=p[k//3][k%3]
 a=[p[0][1],p[1][0]][p[0][1]==p[0][0]];exec(f"f[:]=zip(*eval(str(f).replace('{t}, {a}, {s}','{t},{a},{a}').replace('{a}, {a}, {s}','{a},{a},{a}'))[::-1]);"*60);return f