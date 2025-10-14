def p(n,r=range):
 e=n[0][0];p=sorted((sum(n,[]).count(t),t)for t in r(10)if t!=e);d=p[-1][1];s=[t for p,t in p if f'{t}, {d}'in str(n) and t!=d][0]
 for t in r(900):
  if n[t//30][t%30]==s:
   f=[p[t%30-1:t%30+2]for p in n[t//30-1:t//30+2]]
   if(d in sum(f,[])or e==f[0][1])^1:
    p=[p[t%30-1:t%30+2]for p in n[t//30-1:t//30+2]]
    for o in r(25):n[t//30-2+o//5][t%30-2+o%5]=e
 p=eval(str(p).replace(str(e),str(d)));f=eval(str(n))
 for t in r(900):
  for o in r((n[t//30][t%30]==s)*9):f[t//30-1+o//3][t%30-1+o%3]=p[o//3][o%3]
 e=[p[0][1],p[1][0]][p[0][1]==p[0][0]];exec(f"f[:]=zip(*eval(str(f).replace('{s}, {e}, {d}','{s},{e},{e}').replace('{e}, {e}, {d}','{e},{e},{e}'))[::-1]);"*60);return f